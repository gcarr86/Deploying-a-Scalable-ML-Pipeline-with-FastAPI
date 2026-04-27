# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

Model Details
This model is a LogisticRegression classifier trained to predict whether an individual earns more than $50K per year based on demographic and employment‑related features from the U.S. Census Income dataset.
The model was developed using Python, scikit‑learn, and the starter code provided by Udacity/WGU.
Model artifacts, including the trained model, encoder, and label binarizer, are stored in the model directory.
Intended Use
This model is intended for educational purposes. It demonstrates how to build a reproducible machine learning pipeline, train and evaluate a classification model, deploy a model using FastAPI, and compute slice‑based performance metrics.
The model is not intended for real‑world decision‑making, including hiring, credit scoring, financial decisions, or any high‑stakes or legally sensitive applications.
Training Data
The model was trained on the Census Income dataset. The dataset includes features such as age, education, occupation, marital status, work class, race, and sex.
Preprocessing steps included cleaning whitespace and formatting, encoding categorical variables, scaling numerical features, and splitting the data into training and test sets.
Evaluation Data
Evaluation was performed on the held‑out test split of the Census dataset.
The same preprocessing steps used during training were applied during evaluation to ensure consistency.
Metrics
The model was evaluated on the test dataset using standard classification metrics.
Precision: 0.7306
Recall: 0.5646
F1 Score: 0.6370
Slice‑based metrics were also generated to evaluate performance across demographic subgroups. These results were saved to the file slice_output.txt.
Ethical Considerations
The Census dataset contains sensitive demographic attributes such as race and sex, which may introduce bias into the model.
Predictions may be less accurate for certain demographic groups, making the model unsuitable for real‑world decision‑making.
Slice metrics help identify potential fairness issues but do not eliminate them.
The model should not be used in any context where biased predictions could cause harm.
Caveats and Recommendations
The model is trained only on U.S. Census data and may not generalize to other populations.
Retraining is recommended if the dataset changes or if new demographic patterns appear.
Human oversight is required for any interpretation of predictions.
This model is for demonstration and learning purposes only and should not be deployed in production environments.