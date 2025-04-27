# Re-Align Workshop Hackathon

This hackathon focuses on understanding and comparing representational alignment across a wide variety of vision models. Participants will join either the Blue Team or the Red Team and provide JSON submissions that demonstrate the largest uniform set of models (Blue) or greatest differentiation among those models (Red).

Hackathon Overview
We have ~1300 vision models available for use, plus metadata about each model’s architecture, training data, and more. The hackathon aims to answer:

When are models “functionally identical” (indistinguishable) in their behaviors?
When do models show meaningful differences—and how can we highlight those differences with carefully chosen stimuli?
Key points:

## Team Objectives

### 🟦 Blue Team:
Identify universal patterns across models by finding sets that function identically on selected stimuli.

- **Objective**: Submit a collection of models that demonstrate functional equivalence when processing the same stimulus set.
- **Challenge**: Find surprising similarities among seemingly different architectures.

### 🟥 Red Team:
Uncover meaningful functional differences between models by carefully selecting diagnostic stimuli.

- **Objective**: Curate stimuli that reveal significant functional differences between model groups.
- **Challenge**: Identify the most informative test cases that highlight meaningful variation.

## Submission Requirements
Your final submission must be in JSON format. The submission should document:
1. Your methodology for identifying similar models (Blue) or selecting revealing stimuli (Red)
2. A concise rationale explaining your findings
3. Supporting evidence for your conclusions

For more detailed instructions, look below

We look forward to discovering insights about representational alignment - whether through unexpected uniformity or revealing differences between models.


## Submission Instructions

- **File Type**: JSON
- **File Name**: `team_name.json` (replace "team_name" with your actual team name)
- **File Location**: Place your submission in the `{blue/red}_team_submissions/` directory

### Blue Team JSON format

```json
{
  "models": [
    {
      "model_name": "model1_name",
      "source": "where the model is from",
      "model_parameters": {
        "param1": "value1",
        "param2": "value2"
      }
    },
    {
      "model_name": "model2_name",
      "source": "where the model is from",
      "model_parameters": null
    }
  ]
}
```

### Red Team JSON format

```json
{
  "differentiating_images": [
    {
      "dataset_name": "cifar100",
      "image_identifier": "test/girl/image_987.png"
    },
    {
      "dataset_name": "cifar100",
      "image_identifier": "test/orange/image_19.png"
    },
    {
      "dataset_name": "cifar100",
      "image_identifier": "test/bottle/image_2428.png"
    }
    // … add as many entries as needed
  ]
}
```

**Field descriptions**

| Key | Purpose | Example |
|-----|---------|---------|
| `dataset_name` | Name of the public dataset the stimulus comes from. | `"cifar100"` |
| `image_identifier` | Path or unique identifier that locates the file within your submission’s `stimuli/` directory. | `"test/girl/image_987.png"` |

Notes:
- Include **exactly** these two keys for every stimulus object.  
- Ensure every `(dataset_name, image_identifier)` pair is **unique**.

### Setup & Submission (Applies to **Both Blue and Red Teams**)

#### 1&nbsp;—&nbsp;Fork and Clone
1. **Fork** this repository on GitHub:

2. **Clone** your fork and create a branch for your submission (replace `<team_color>` with either `blue` or `red`):
   ```bash
   git clone [PATH_TO_YOUR_FORK]
   cd realign-metrics
   git checkout main  
   git pull origin main  
   git checkout -b <team_color>_team_submissions
   git checkout -b <team_color>_team_winning_submission
   ```

#### 2 — Prepare Your Submission
| Team | Place the file(s) in | Required main file | Commit message title example |
|------|----------------------|--------------------|------------------------------|
| **Blue** | `blue_team_submissions/` | `team_name.json` | `Blue Team Submission: [team_name]` |
| **Red** | `red_team_submissions/` | `team_name.json` | `Red Team Submission: [team_name]` |

#### 3 — Commit & Push
```bash
git add [your files]
git commit -m "<Blue or Red> Team Submission: [team_name]"
git push --set-upstream origin {blue/red}_team_submissions
```

#### 4 — Open a Pull Request
1. Go to your fork on GitHub.
2. Click **"Compare & pull request."**
3. Select the base branch to merge into: `<team_color>_team_submissions`
4. Use the title:  
   - `Blue Team: [team_name]` **or**  
   - `Red Team: [team_name]`
5. Submit — you’re done! 🎉


## Getting Started

### Setting Up a Conda Environment

You can set up a conda environment for this project using either the `pyproject.toml` file or the `requirements.txt` file.

#### Using requirements.txt

```bash
# Create a new conda environment
conda create -n realign-metrics python=3.9
conda activate realign-metrics

# Install requirements
pip install -r requirements.txt
```

#### Using pyproject.toml

```bash
# Create a new conda environment
conda create -n realign-metrics python=3.9
conda activate realign-metrics

# Install project in development mode
pip install -e .
```

This will install all the necessary dependencies for you to run the code in this repository.


## Example Notebooks and Starter Code

We've provided starter notebooks to help you get started with the hackathon. These can be found in the `examples/` folder:

### Common Resources
- **`extract_activations.ipynb`**: Demonstrates how to extract model activations, which is useful for both Blue and Red teams.

### Team-Specific Starter Code
- **Blue Team**: `blue_team_starter.ipynb` - Guides you through the process of identifying model similarities across different models.
- **Red Team**: `red_team_starter.ipynb` - Helps you discover and analyze stimuli that reveal meaningful differences between model representations.

These notebooks contain code examples, visualization tools, and methodological suggestions to kickstart your approach to the challenge.