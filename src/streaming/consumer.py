
from kafka import KafkaConsumer
import json
import pandas as pd
import joblib

from src.utils.database import SessionLocal
from src.database.models import FraudAlert

# Load trained model
model = joblib.load(
    "models/streaming_fraud_model.pkl"
)

consumer = KafkaConsumer(
    "transactions",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    value_deserializer=lambda m: json.loads(
        m.decode("utf-8")
    )
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

    fraud_probability = float(
        model.predict_proba(features)[0][1]
    )

    risk_score = float(
        round(
            fraud_probability * 100,
            2
        )
    )

    prediction_label = (
        "FRAUD"
        if prediction == 1
        else "GENUINE"
    )

    db = SessionLocal()

    try:

        alert = FraudAlert(
            amount=float(tx["amount"]),
            merchant_id=int(tx["merchant_id"]),
            hour=int(tx["hour"]),
            risk_score=risk_score,
            prediction=prediction_label
        )

        db.add(alert)
        db.commit()

        print(
            {
                "amount": tx["amount"],
                "merchant_id": tx["merchant_id"],
                "hour": tx["hour"],
                "risk_score": risk_score,
                "prediction": prediction_label
            }
        )

    except Exception as e:

        db.rollback()

        print(
            f"Database Error: {e}"
        )

    finally:

        db.close()