import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="Real-Time Fraud Detection Dashboard",
    page_icon="🚨",
    layout="wide"
)

st.title("🚨 Real-Time Fraud Detection Dashboard")

file_path = "fraud_alerts.csv"

if os.path.exists(file_path):

    df = pd.read_csv(file_path)

    if len(df) > 0:

        total_transactions = len(df)

        frauds = len(
            df[df["prediction"] == "FRAUD"]
        )

        fraud_rate = round(
            (frauds / total_transactions) * 100,
            2
        )

        avg_risk_score = round(
            df["risk_score"].mean(),
            2
        )

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            "Total Transactions",
            total_transactions
        )

        col2.metric(
            "Fraud Alerts",
            frauds
        )

        col3.metric(
            "Fraud Rate (%)",
            fraud_rate
        )

        col4.metric(
            "Average Risk Score",
            avg_risk_score
        )

        st.divider()

        st.subheader("Recent Transactions")

        st.dataframe(
            df.tail(20),
            use_container_width=True
        )

        st.divider()

        col1, col2 = st.columns(2)

        with col1:

            st.subheader("Risk Score Trend")

            st.line_chart(
                df["risk_score"].tail(100)
            )

        with col2:

            st.subheader("Fraud vs Genuine")

            prediction_counts = (
                df["prediction"]
                .value_counts()
            )

            st.bar_chart(
                prediction_counts
            )

        st.divider()

        st.subheader("High-Risk Transactions")

        high_risk = df[
            df["risk_score"] >= 80
        ]

        if len(high_risk) > 0:

            st.dataframe(
                high_risk.tail(20),
                use_container_width=True
            )

        else:

            st.success(
                "No high-risk transactions detected."
            )

    else:

        st.warning(
            "No transactions available yet."
        )

else:

    st.warning(
        "Waiting for fraud_alerts.csv..."
    )

st.caption(
    "Real-Time Fraud Detection System | Kafka + XGBoost + FastAPI + Streamlit"
)