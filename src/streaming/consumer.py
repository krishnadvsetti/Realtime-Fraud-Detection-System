import json

import joblib
import pandas as pd
from kafka import KafkaConsumer

from src.database.models import FraudAlert
from src.utils.config import (
    KAFKA_AUTO_OFFSET_RESET,
    KAFKA_BOOTSTRAP_SERVERS,
    KAFKA_GROUP_ID,
    KAFKA_TOPIC,
    MODEL_PATH,
)
from src.utils.database import SessionLocal
from src.utils.logger import logger


model = joblib.load(MODEL_PATH)

consumer = KafkaConsumer(
    KAFKA_TOPIC,
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    group_id=KAFKA_GROUP_ID,
    auto_offset_reset=KAFKA_AUTO_OFFSET_RESET,
    value_deserializer=lambda m: json.loads(
        m.decode("utf-8")
    )
)

logger.info("ML Fraud Detection Consumer Started")


try:

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

        risk_score = round(
            fraud_probability * 100,
            2
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
                risk_score=float(risk_score),
                prediction=prediction_label
            )

            db.add(alert)
            db.commit()

            logger.info(
                f"Prediction={prediction_label} "
                f"Risk={risk_score:.2f}% "
                f"Amount={tx['amount']}"
            )

        except Exception as e:

            db.rollback()
            logger.exception(e)

        finally:

            db.close()

except KeyboardInterrupt:

    logger.info("Kafka Consumer Stopped")

finally:

    consumer.close()