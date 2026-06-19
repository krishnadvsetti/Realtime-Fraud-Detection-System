from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, text
import pandas as pd

app = FastAPI(
    title="Real-Time Fraud Detection API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

DATABASE_URL = "postgresql://frauduser:fraudpass@localhost:5432/frauddb"

engine = create_engine(DATABASE_URL)


@app.get("/")
def root():
    return {"status": "Fraud Detection API Running"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/metrics")
def metrics():

    df = pd.read_sql(
        text("SELECT * FROM fraud_alerts"),
        engine
    )

    total = len(df)

    frauds = len(
        df[df["prediction"] == "FRAUD"]
    )

    fraud_rate = (
        round((frauds / total) * 100, 2)
        if total else 0
    )

    avg_risk = (
        round(df["risk_score"].mean(), 2)
        if total else 0
    )

    return {
        "total_transactions": total,
        "fraud_alerts": frauds,
        "fraud_rate": fraud_rate,
        "avg_risk_score": avg_risk
    }


@app.get("/transactions")
def transactions():

    df = pd.read_sql(
        text("""
        SELECT *
        FROM fraud_alerts
        ORDER BY id DESC
        LIMIT 100
        """),
        engine
    )

    return df.to_dict(orient="records")


@app.get("/fraud-summary")
def fraud_summary():

    df = pd.read_sql(
        text("""
        SELECT prediction,
               COUNT(*) AS count
        FROM fraud_alerts
        GROUP BY prediction
        """),
        engine
    )

    return df.to_dict(orient="records")