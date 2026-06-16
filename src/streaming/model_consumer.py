import joblib
import pandas as pd
import json

from kafka import KafkaConsumer

model = joblib.load(
    "models/xgboost_model.pkl"
)

consumer = KafkaConsumer(
    "transactions",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="latest",
    value_deserializer=lambda m:
        json.loads(m.decode("utf-8"))
)

print("ML Fraud Consumer Started")