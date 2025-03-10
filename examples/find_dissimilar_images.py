from sklearn.metrics import pairwise_distances
import os
import random
from PIL import Image
from matplotlib.gridspec import GridSpec
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.manifold import MDS
from scipy.spatial import procrustes
import numpy as np

from thingsvision.core.cka import CKA
from thingsvision.core.rsa import compute_rdm, correlate_rdms
from itertools import combinations, product
from sklearn.decomposition import PCA

def compare_random_image_groups(activation_dir, dataset_name, models, num_groups=5, images_per_group=20, methods=None):
    """
    Compare random groups of images using different alignment metrics.
    """
    # Load file names
    fnames = np.loadtxt(f'{activation_dir}/{dataset_name}/file_names.txt', dtype=str)
    
    # Default methods if not specified
    if methods is None:
        methods = ['cka', 'rsa', 'procrustes']
        
    # Create random groups
    num_images = len(fnames)
    groups = {}
    for i in range(num_groups):
        groups[i] = np.array(random.sample(range(num_images), images_per_group))
    
    # Initialize results dictionary
    results = {method: np.zeros(num_groups) for method in methods}
    
    # For each model pair, compute alignment metrics for each group
    for method in methods:
        metric_values = []
        
        for idx, (model1, model2) in enumerate(combinations(models, 2)):
            print(f"Processing model pair for {method}: {model1['model_name']} vs {model2['model_name']}")
            
            for layer1, layer2 in product(model1['layers_to_extract'], model2['layers_to_extract']):
                features1 = np.load(f'{activation_dir}/{dataset_name}/{model1["model_name"]}/{layer1}/features.npy')
                features2 = np.load(f'{activation_dir}/{dataset_name}/{model2["model_name"]}/{layer2}/features.npy')
                
                # Apply PCA if needed
                if features1.shape[1] > 50:
                    pca1 = PCA(n_components=50)
                    pca2 = PCA(n_components=50)
                    features1 = pca1.fit_transform(features1)
                    features2 = pca2.fit_transform(features2)
                
                # Calculate metric for each group
                group_metrics = np.zeros(num_groups)
                
                for i in range(num_groups):
                    group_idx = groups[i]
                    
                    # Extract features for this group
                    group_features1 = features1[group_idx]
                    group_features2 = features2[group_idx]
                    
                    # Compute metric for this group
                    if method == 'cka':
                        cka = CKA(m=len(group_idx), kernel='linear')
                        similarity = cka.compare(X=group_features1, Y=group_features2)
                        group_metrics[i] = 1 - similarity  # Convert to dissimilarity
                        
                    elif method == 'rsa':
                        rdm1 = compute_rdm(group_features1, method='correlation')
                        rdm2 = compute_rdm(group_features2, method='correlation')
                        correlation = correlate_rdms(rdm1, rdm2, correlation='pearson')
                        group_metrics[i] = 1 - correlation  # Convert to dissimilarity
                        
                    elif method == 'procrustes':
                        dist1 = pairwise_distances(group_features1)
                        dist2 = pairwise_distances(group_features2)
                        _, _, disparity = procrustes(dist1, dist2)
                        group_metrics[i] = disparity
                
                metric_values.append(group_metrics)
        
        # Average across all model pairs
        results[method] = np.mean(np.array(metric_values), axis=0)
    
    return groups, results, fnames

def rank_groups_by_dissimilarity(results):
    """
    Rank groups by dissimilarity for each metric.
    """
    rankings = {}
    
    for method, scores in results.items():
        # Sort by dissimilarity (high to low)
        sorted_indices = np.argsort(-scores)
        
        # Create ranking dictionary
        method_rankings = {}
        for rank, idx in enumerate(sorted_indices):
            method_rankings[idx] = {
                'rank': rank + 1,
                'score': scores[idx]
            }
        
        rankings[method] = method_rankings
    
    return rankings

def visualize_results(groups, results, rankings, fnames, output_dir):
    """
    Visualize results and sample images from each group.
    """
    os.makedirs(output_dir, exist_ok=True)
    
    # Create summary plot
    fig = plt.figure(figsize=(15, 4 * len(groups)))
    gs = GridSpec(len(groups), 5, figure=fig)  # 5 sample images per group
    
    for group_id, image_indices in groups.items():
        # Create ranking info string
        ranking_info = " | ".join([
            f"{method.upper()}: {results[method][group_id]:.3f} (Rank: {rankings[method][group_id]['rank']})"
            for method in results.keys()
        ])
        
        # Select sample images
        sample_indices = random.sample(list(image_indices), min(5, len(image_indices)))
        
        for i, img_idx in enumerate(sample_indices):
            img_path = fnames[img_idx]
            try:
                img = Image.open(img_path)
                ax = fig.add_subplot(gs[group_id, i])
                ax.imshow(img)
                if i == 0:
                    ax.set_title(f"Group {group_id}\n{ranking_info}", fontsize=10)
                ax.axis('off')
            except Exception as e:
                print(f"Error loading image {img_path}: {e}")
                continue
    
    plt.tight_layout()
    plt.savefig(f"{output_dir}/group_comparison.png", dpi=300)
    plt.close(fig)
    
    # Create bar chart for dissimilarity rankings
    methods = list(results.keys())
    fig, axes = plt.subplots(len(methods), 1, figsize=(10, 3 * len(methods)))
    
    for i, method in enumerate(methods):
        scores = results[method]
        ax = axes[i] if len(methods) > 1 else axes
        ax.bar(range(len(scores)), scores)
        ax.set_title(f"{method.upper()} Dissimilarity")
        ax.set_xticks(range(len(scores)))
        ax.set_xticklabels([f"Group {j} (Rank {rankings[method][j]['rank']})" for j in range(len(scores))])
    
    plt.tight_layout()
    plt.savefig(f"{output_dir}/dissimilarity_rankings.png", dpi=300)
    plt.close(fig)

def main():
    """
    Main function to compare random image groups.
    """
    activation_dir = '../activations'
    dataset_name = 'cifar100'
    output_dir = './random_group_analysis'
    
    # Define models
    models = [
        {'model_name': 'resnet50', 'source': 'torchvision', 'model_parameters': None, 'layers_to_extract': ['fc']},
        {'model_name': 'mocov2-rn50', 'source': 'ssl', 'model_parameters': None, 'layers_to_extract': ['fc']},
        {'model_name': 'clip', 'source': 'custom', 'model_parameters': {'variant': 'ViT-B/32'}, 'layers_to_extract': ['visual']},
        {'model_name': 'alexnet', 'source': 'torchvision', 'model_parameters': None, 'layers_to_extract': ['classifier.4']}
    ]
    
    # Methods to compare
    methods = ['cka', 'rsa', 'procrustes']
    
    # Compare random image groups
    print("Comparing 5 random groups of 20 images each...")
    groups, results, fnames = compare_random_image_groups(
        activation_dir, dataset_name, models, 
        num_groups=5, images_per_group=20,
        methods=methods
    )
    
    # Rank groups by dissimilarity
    rankings = rank_groups_by_dissimilarity(results)
    
    # Print results
    print("\nDissimilarity scores for each group:")
    for method in methods:
        print(f"\n{method.upper()}:")
        for group_id in range(len(groups)):
            rank = rankings[method][group_id]['rank']
            print(f"  Group {group_id}: {results[method][group_id]:.4f} (Rank: {rank})")
    
    # Visualize results
    visualize_results(groups, results, rankings, fnames, output_dir)
    
    # Export to CSV
    df_results = pd.DataFrame({f"{method}_score": results[method] for method in methods})
    df_results['group_id'] = range(len(groups))
    for method in methods:
        df_results[f"{method}_rank"] = [rankings[method][i]['rank'] for i in range(len(groups))]
    df_results.to_csv(f"{output_dir}/group_analysis_results.csv", index=False)
    print(f"Results saved to {output_dir}/group_analysis_results.csv")

if __name__ == "__main__":
    main()
