import streamlit as st
import pandas as pd
import os

st.title("🚨 Real-Time Fraud Monitoring Dashboard")

if os.path.exists("fraud_alerts.csv"):

    df = pd.read_csv("fraud_alerts.csv")

    st.metric(
        "Total Transactions",
        len(df)
    )

    frauds = len(
        df[df["prediction"] == "FRAUD"]
    )

    st.metric(
        "Fraud Alerts",
        frauds
    )

    st.metric(
        "Fraud Rate (%)",
        round((frauds / len(df)) * 100, 2)
    )

    st.dataframe(df.tail(20))

    st.bar_chart(df["risk_score"])

else:
    st.warning("Waiting for transactions...")