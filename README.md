# realign-metrics


Re-Align Workshop Hackathon
This hackathon focuses on understanding and comparing representational alignment across a wide variety of vision models. Participants will join either the Blue Team or the Red Team and provide JSON submissions that demonstrate the largest uniform set of models (Blue) or greatest differentiation among those models (Red).

Hackathon Overview
We have ~1300 vision models available for use, plus metadata about each model’s architecture, training data, and more. The hackathon aims to answer:

When are models “functionally identical” (indistinguishable) in their behaviors?
When do models show meaningful differences—and how can we highlight those differences with carefully chosen stimuli?
Key points:

## Team Objectives

- **Blue Team**: Identify universal patterns across models by finding sets that function identically on selected stimuli.
- **Red Team**: Uncover meaningful functional differences between models by carefully selecting diagnostic stimuli.

## Hackathon Goal

### Blue Team
- **Objective**: Submit a collection of models that demonstrate functional equivalence when processing the same stimulus set.
- **Challenge**: Find surprising similarities among seemingly different architectures.

### Red Team
- **Objective**: Curate stimuli that reveal significant functional differences between model groups.
- **Challenge**: Identify the most informative test cases that highlight meaningful variation.

## Submission Requirements
Your final submission must be in JSON format for the Blue Team and a zip file for the Red team. The submission should document:
1. Your methodology for identifying similar models (Blue) or selecting revealing stimuli (Red)
2. A concise rationale explaining your findings
3. Supporting evidence for your conclusions

For more detailed instructions, look below

We look forward to discovering insights about representational alignment - whether through unexpected uniformity or revealing differences between models.


## Submission Instructions

### Blue Team Submissions

#### Submission Format
- **File Type**: JSON
- **File Name**: `team_name.json` (replace "team_name" with your actual team name)
- **File Location**: Place your submission in the `blue_team_submissions/` directory
- **JSON Structure**: Your submission must follow this format:
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
#### ✅ Validation Requirements

To ensure compatibility with the activation extraction pipeline, your submission must meet the following requirements:

- Each model must have a **unique** `model_name` within your submission.
- Each model entry must include the following fields:
  - `model_name`
  - `source`
  - `model_parameters`
- The `model_parameters` field can be set to `null` if no parameters are specified.
- The file must be in **valid JSON** format.

These parameters (`model_name`, `source`, and `model_parameters`) are used to extract activations from your model via:

- [`extract_activations.ipynb`](./extract_activations.ipynb)
- Starter notebooks located in:
  - [`red_team_submissions/`](./red_team_submissions/)
  - [`blue_team_submissions/`](./blue_team_submissions/)

The activation extraction process relies on [`thingsvision`](https://github.com/MECLabTUDA/ThingsVision), which supports a variety of pre-trained models listed [here](https://thingsvision.github.io/AvailableModels.html).


#### Setup
1. First, [fork the repository](https://docs.github.com/en/get-started/quickstart/fork-a-repo) in GitHub:
    <a href="https://docs.github.com/en/get-started/quickstart/fork-a-repo">
    <div style="text-align:center"><img src="https://docs.github.com/assets/images/help/repository/fork_button.png" alt="fork button" width="500"/></div>
    </a>

2. Clone your fork and create a branch for your submission:
    ```bash
    git clone [PATH_TO_YOUR_FORK]
    cd realign-metrics
    git checkout -b blue_team_winning_submission
    ```

#### Submitting
1. Prepare your JSON submission according to the requirements.
2. Add and commit your files:
    ```bash
    git add [your files]
    git commit -m "Blue Team Submission: [team_name]"
    git push --set-upstream origin blue_team_winning_submission
    ```
3. [Create a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) with the title "Blue Team: [team_name]"

### Red Team Submissions

#### Setup
1. First, [fork the repository](https://docs.github.com/en/get-started/quickstart/fork-a-repo) in GitHub.
2. Clone your fork and create a branch for your submission:
    ```bash
    git clone [PATH_TO_YOUR_FORK]
    cd realign-metrics
    git checkout -b red_team_winning_submission
    ```

#### Submitting
1. Prepare your zip file containing your stimuli and supporting documentation.
2. Add and commit your files:
    ```bash
    git add [your files]
    git commit -m "Red Team Submission: [team_name]"
    git push --set-upstream origin red_team_winning_submission
    ```
3. [Create a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/- **File Name**: `team_name.json`
- **Content**: The JSON file should include:
  - A list of model names (or IDs) that are functionally identical
  - A description of the stimuli used to test the models
  - A brief explanation of the methodology used to identify the models as functionally identical
  - Any relevant metadata about the models (e.g., architecture, training data)proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) with the title "Red Team: [team_name]"

All submissions will be reviewed by the organizers. Good luck!

