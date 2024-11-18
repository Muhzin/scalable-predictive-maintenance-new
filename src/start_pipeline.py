# src/start_pipeline.py

import subprocess

def run_pipeline():
    subprocess.run(['python', 'src/data_preprocessing.py'])
    subprocess.run(['python', 'src/model_training.py'])
    subprocess.run(['python', 'src/kafka_consumer.py'])
    subprocess.run(['python', 'src/model_evaluation.py'])

if __name__ == "__main__":
    run_pipeline()

