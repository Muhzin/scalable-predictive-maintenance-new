# src/model_evaluation.py

from sklearn.metrics import accuracy_score, classification_report
import joblib
import pandas as pd

# Load the model
model = joblib.load('model.joblib')

# Load the test data
test_data = pd.read_csv('path_to_test_data.csv')
X_test = test_data.drop('target_column', axis=1)
y_test = test_data['target_column']

# Predict and evaluate the model
y_pred = model.predict(X_test)

print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
print(f"Classification Report: \n{classification_report(y_test, y_pred)}")

