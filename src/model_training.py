# src/model_training.py

from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import joblib

# Load preprocessed data
data = pd.read_csv("path_to_your_processed_data.csv")
X = data.drop('target_column', axis=1)
y = data['target_column']

# Train the model
model = RandomForestClassifier()
model.fit(X, y)

# Save the trained model
joblib.dump(model, 'model.joblib')

print("Model trained and saved successfully.")

