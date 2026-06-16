from kafka import KafkaConsumer
import json
import pandas as pd
import os
import joblib

model = joblib.load(
    "models/streaming_fraud_model.pkl"
)

consumer = KafkaConsumer(
    "transactions",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    value_deserializer=lambda m:
        json.loads(m.decode("utf-8"))
)

print("ML Fraud Detection Started")

for msg in consumer:

    tx = msg.value

    features = pd.DataFrame(
        [[
            tx["amount"],
            tx["merchant_id"],
            tx["hour"]
        ]],
        columns=[
            "amount",
            "merchant_id",
            "hour"
        ]
    )

    prediction = model.predict(features)[0]

    fraud_probability = (
        model.predict_proba(features)[0][1]
    )

    risk_score = round(
        fraud_probability * 100,
        2
    )

    prediction_label = (
        "FRAUD"
        if prediction == 1
        else "GENUINE"
    )

    record = {
        "amount": tx["amount"],
        "merchant_id": tx["merchant_id"],
        "hour": tx["hour"],
        "risk_score": risk_score,
        "prediction": prediction_label
    }

    df = pd.DataFrame([record])

    file_path = "fraud_alerts.csv"

    if os.path.exists(file_path):
        df.to_csv(
            file_path,
            mode="a",
            header=False,
            index=False
        )
    else:
        df.to_csv(
            file_path,
            index=False
        )

    print(record)