from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy import create_engine, text
import pandas as pd

from src.utils.config import DATABASE_URL
from src.utils.logger import logger
from src.explainability.shap_explainer import explainer


app = FastAPI(
    title="Real-Time Fraud Detection API",
    version="1.0.0",
    description="Real-Time Fraud Detection System using FastAPI, Kafka, PostgreSQL, XGBoost and SHAP Explainability."
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

engine = create_engine(DATABASE_URL)


class TransactionRequest(BaseModel):
    amount: float
    merchant_id: int
    hour: int


@app.get(
    "/",
    summary="Application Status",
    description="Returns the application name, version and running status."
)
def root():
    return {
        "application": "Real-Time Fraud Detection System",
        "status": "Running",
        "version": "1.0.0"
    }


@app.get(
    "/health",
    summary="Health Check",
    description="Checks whether the API service is running."
)
def health():
    return {
        "status": "healthy"
    }


@app.get(
    "/metrics",
    summary="Fraud Detection Metrics",
    description="Returns total transactions, fraud count, fraud rate and average risk score."
)
def metrics():

    try:

        with engine.connect() as connection:

            df = pd.read_sql(
                text("SELECT * FROM fraud_alerts"),
                connection
            )

        total = len(df)

        frauds = len(
            df[df["prediction"] == "FRAUD"]
        )

        fraud_rate = round(
            (frauds / total) * 100,
            2
        ) if total else 0

        avg_risk = round(
            df["risk_score"].mean(),
            2
        ) if total else 0

        return {
            "total_transactions": total,
            "fraud_alerts": frauds,
            "fraud_rate": fraud_rate,
            "avg_risk_score": avg_risk
        }

    except Exception as e:

        logger.exception(e)

        raise HTTPException(
            status_code=500,
            detail="Unable to fetch metrics."
        )


@app.get(
    "/transactions",
    summary="Recent Transactions",
    description="Returns the latest 100 fraud detection records."
)
def transactions():

    try:

        with engine.connect() as connection:

            df = pd.read_sql(
                text("""
                SELECT *
                FROM fraud_alerts
                ORDER BY id DESC
                LIMIT 100
                """),
                connection
            )

        return df.to_dict(
            orient="records"
        )

    except Exception as e:

        logger.exception(e)

        raise HTTPException(
            status_code=500,
            detail="Unable to fetch transactions."
        )


@app.get(
    "/fraud-summary",
    summary="Fraud Summary",
    description="Returns the count of FRAUD and GENUINE transactions."
)
def fraud_summary():

    try:

        with engine.connect() as connection:

            df = pd.read_sql(
                text("""
                SELECT prediction,
                       COUNT(*) AS count
                FROM fraud_alerts
                GROUP BY prediction
                """),
                connection
            )

        return df.to_dict(
            orient="records"
        )

    except Exception as e:

        logger.exception(e)

        raise HTTPException(
            status_code=500,
            detail="Unable to fetch fraud summary."
        )


@app.post(
    "/predict",
    summary="Predict Fraud",
    description="Predicts whether a transaction is fraudulent and returns SHAP feature explanations."
)
def predict(transaction: TransactionRequest):

    try:

        return explainer.explain(
            transaction.model_dump()
        )

    except Exception as e:

        logger.exception(e)

        raise HTTPException(
            status_code=500,
            detail="Prediction failed."
        )