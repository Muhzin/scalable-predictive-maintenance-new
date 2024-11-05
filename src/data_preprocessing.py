# src/data_preprocessing.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def load_data(file_path):
    return pd.read_csv(file_path)

def preprocess_data(df):
    df = df.fillna(df.mean())
    features = df.drop('failure', axis=1)
    scaler = StandardScaler()
    return scaler.fit_transform(features), df['failure']

def split_data(X, y):
    return train_test_split(X, y, test_size=0.2, random_state=42)

