from kafka import KafkaConsumer
import json
import pandas as pd
import os

consumer = KafkaConsumer(
    "transactions",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    value_deserializer=lambda m: json.loads(m.decode("utf-8"))
)

print("Fraud Detection Started")

for msg in consumer:

    tx = msg.value

    risk_score = 0

    if tx["amount"] > 4000:
        risk_score += 50

    if tx["hour"] < 5:
        risk_score += 30

    if tx["merchant_id"] > 90:
        risk_score += 20

    prediction = (
        "FRAUD"
        if risk_score >= 50
        else "GENUINE"
    )

    record = {
        "amount": tx["amount"],
        "merchant_id": tx["merchant_id"],
        "hour": tx["hour"],
        "risk_score": risk_score,
        "prediction": prediction
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