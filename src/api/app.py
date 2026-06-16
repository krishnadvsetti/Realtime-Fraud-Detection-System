from fastapi import FastAPI
from pydantic import BaseModel

import joblib
import pandas as pd

app = FastAPI()

model = joblib.load("models/xgboost_model.pkl")


class Transaction(BaseModel):
    features: list


@app.get("/")
def home():
    return {"status": "Fraud Detection API Running"}


@app.post("/predict")
def predict(transaction: Transaction):

    df = pd.DataFrame(
        [transaction.features]
    )

    prediction = model.predict(df)[0]

    probability = model.predict_proba(df)[0][1]

    return {
        "prediction": int(prediction),
        "fraud_probability": float(probability)
    }