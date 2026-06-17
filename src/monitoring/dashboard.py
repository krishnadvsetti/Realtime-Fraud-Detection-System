
import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

st.set_page_config(
    page_title="Real-Time Fraud Detection Dashboard",
    page_icon="🚨",
    layout="wide"
)

st.title("🚨 Real-Time Fraud Detection Dashboard")

DATABASE_URL = (
    "postgresql://frauduser:fraudpass@localhost:5432/frauddb"
)

try:

    engine = create_engine(DATABASE_URL)

    df = pd.read_sql(
        "SELECT * FROM fraud_alerts ORDER BY id DESC",
        engine
    )

    if len(df) > 0:

        total_transactions = len(df)

        fraud_count = len(
            df[df["prediction"] == "FRAUD"]
        )

        fraud_rate = round(
            (fraud_count / total_transactions) * 100,
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
            fraud_count
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

        st.subheader(
            "Recent Transactions"
        )

        st.dataframe(
            df.head(20),
            use_container_width=True
        )

        st.divider()

        col1, col2 = st.columns(2)

        with col1:

            st.subheader(
                "Risk Score Trend"
            )

            st.line_chart(
                df["risk_score"].head(100)
            )

        with col2:

            st.subheader(
                "Fraud vs Genuine"
            )

            prediction_counts = (
                df["prediction"]
                .value_counts()
            )

            st.bar_chart(
                prediction_counts
            )

        st.divider()

        st.subheader(
            "High Risk Transactions"
        )

        high_risk = df[
            df["risk_score"] >= 50
        ]

        if len(high_risk) > 0:

            st.dataframe(
                high_risk.head(20),
                use_container_width=True
            )

        else:

            st.success(
                "No high-risk transactions detected."
            )

    else:

        st.warning(
            "No transactions found in database."
        )

except Exception as e:

    st.error(
        f"Database Error: {e}"
    )

st.caption(
    "Kafka + XGBoost + PostgreSQL + FastAPI + Streamlit + MLflow"
)
