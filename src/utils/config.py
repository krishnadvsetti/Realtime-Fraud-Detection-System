import os
from dotenv import load_dotenv

load_dotenv()


def get_env(key: str, default=None, required: bool = False):
    value = os.getenv(key, default)

    if required and (value is None or value == ""):
        raise ValueError(f"Environment variable '{key}' is not set.")

    return value


# ==========================================
# Application
# ==========================================

APP_NAME = get_env(
    "APP_NAME",
    "Real-Time Fraud Detection System"
)

APP_VERSION = get_env(
    "APP_VERSION",
    "1.0.0"
)

DEBUG = get_env(
    "DEBUG",
    "False"
).lower() == "true"


# ==========================================
# FastAPI
# ==========================================

API_HOST = get_env(
    "API_HOST",
    "0.0.0.0"
)

API_PORT = int(
    get_env(
        "API_PORT",
        8000
    )
)


# ==========================================
# PostgreSQL
# ==========================================

DATABASE_URL = get_env(
    "DATABASE_URL",
    required=True
)


# ==========================================
# Kafka
# ==========================================

KAFKA_BOOTSTRAP_SERVERS = get_env(
    "KAFKA_BOOTSTRAP_SERVERS",
    "localhost:9092"
)

KAFKA_TOPIC = get_env(
    "KAFKA_TOPIC",
    "transactions"
)

KAFKA_GROUP_ID = get_env(
    "KAFKA_GROUP_ID",
    "fraud-consumer-group"
)

KAFKA_AUTO_OFFSET_RESET = get_env(
    "KAFKA_AUTO_OFFSET_RESET",
    "earliest"
)


# ==========================================
# Machine Learning
# ==========================================

MODEL_PATH = get_env(
    "MODEL_PATH",
    "models/streaming_fraud_model.pkl"
)


# ==========================================
# Dashboard
# ==========================================

REFRESH_INTERVAL = int(
    get_env(
        "REFRESH_INTERVAL",
        5
    )
)