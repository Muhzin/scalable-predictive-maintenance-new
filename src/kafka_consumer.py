# src/kafka_consumer.py

from kafka import KafkaConsumer
import json

# Initialize Kafka Consumer
consumer = KafkaConsumer('maintenance_topic', 
                         group_id='maintenance_group',
                         bootstrap_servers=['localhost:9092'])

# Consume messages from Kafka topic
for message in consumer:
    data = json.loads(message.value)
    print(f"Received data: {data}")
    # Here you can add logic to process the data.

