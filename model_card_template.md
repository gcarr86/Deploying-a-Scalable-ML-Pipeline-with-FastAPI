# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
This model is a supervised machine learning classifier trained to predict whether an individual earns more than $50K per year based on demographic and employment‑related features from the U.S. Census Income dataset.
The model was developed using Python, scikit‑learn, and the project starter code provided by Udacity/WGU.
Model artifacts (trained model, encoder, and label binarizer) are stored in the  directory.

## Intended Use

The model is intended for educational purposes, specifically to demonstrate:
• 	Building a reproducible ML pipeline
• 	Training and evaluating a classification model
• 	Deploying a model using FastAPI
• 	Computing slice‑based performance metrics
Not intended for real‑world decision‑making, including:
• 	Hiring
• 	Credit scoring
• 	Financial decisions
• 	Any high‑stakes or legally sensitive applications
## Training Data

The model was trained on the Census Income dataset, which includes features such as age, education, occupation, marital status, work class, race, and sex.
Data preprocessing steps included:
• 	Cleaning whitespace and formatting
• 	Encoding categorical variables
• 	Scaling numerical features
• 	Splitting into training and test sets
## Evaluation Data
Evaluation was performed on the held‑out test split of the Census dataset.
The same preprocessing steps applied during training were used during evaluation to ensure consistency.
## Metrics
The model was evaluated using:
- Precision
- Recall
- F1 Score
These metrics were computed on the test dataset after training.
Slice‑based metrics were also generated to evaluate performance across subgroups (like, education levels), and results were saved to slice_output.txt


## Ethical Considerations
- The Census dataset contains sensitive demographic attributes (e.g., race, sex), which may introduce bias into the model.
- Predictions may be less accurate for certain demographic groups, making the model unsuitable for real‑world decision‑making.
- Slice metrics help identify potential fairness issues, but they do not eliminate them.
- The model should not be used in any context where biased predictions could cause harm.

## Caveats and Recommendations
- The model is trained only on U.S. Census data and may not generalize to other populations.
- Retraining is recommended if the dataset changes or if new demographic patterns emerge.
- Human oversight is required for any interpretation of predictions.
- This model is for demonstration and learning purposes only and should not be deployed in production environments.
