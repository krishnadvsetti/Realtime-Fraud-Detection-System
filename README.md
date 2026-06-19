
# Real-Time Fraud Detection System

## Overview

A real-time fraud detection platform built using Kafka, XGBoost, FastAPI, Streamlit, Docker, and MLflow.

The system simulates transaction streams, performs fraud scoring in real time, stores fraud alerts, and visualizes operational metrics through an interactive monitoring dashboard.

---

## Architecture

```text
Transaction Generator
        │
        ▼
Kafka Producer
        │
        ▼
Kafka Topic
        │
        ▼
Kafka Consumer
        │
        ▼
XGBoost Fraud Detection Model
        │
        ▼
Fraud Alerts Storage
        │
        ▼
Streamlit Dashboard
```

---

## Features

* Real-time transaction streaming with Kafka
* Fraud detection using XGBoost
* FastAPI model serving
* Interactive Swagger API documentation
* Fraud alert generation and persistence
* Streamlit monitoring dashboard
* MLflow experiment tracking
* Docker-based local deployment

---

## Tech Stack

* Python
* XGBoost
* Kafka
* FastAPI
* Streamlit
* Docker
* MLflow
* Pandas
* Scikit-learn

---

## Project Structure

```text
src/
├── api/
├── data/
├── monitoring/
├── streaming/
├── training/
└── utils/

models/
data/
```

---

## Model Performance

### Credit Card Fraud Dataset

* Precision: 0.75
* Recall: 0.87
* ROC-AUC: 0.982

### Streaming Fraud Model

* Accuracy: 97.99%
* Precision: 99.45%
* Recall: 78.59%
* ROC-AUC: 88.95%

---

## Running the Project

### Start Kafka

```bash
docker compose up -d
```

### Start Consumer

```bash
python src/streaming/consumer.py
```

### Start Producer

```bash
python src/streaming/producer.py
```

### Start Dashboard

```bash
streamlit run src/monitoring/dashboard.py --server.port 8501
```

### Start API

```bash
uvicorn src.api.app:app --reload --host 0.0.0.0 --port 8000
```

### Start MLflow

```bash
mlflow ui --host 0.0.0.0 --port 5000
```

---

## Production Architecture

```text
┌──────────────────────────────┐
│      Transaction Stream      │
│     Synthetic Generator      │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│        Kafka Producer        │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│         Kafka Topic          │
│        transactions          │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│        Kafka Consumer        │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│     XGBoost Fraud Model      │
│  streaming_fraud_model.pkl   │
└──────────────┬───────────────┘
               │
      ┌────────┴────────┐
      │                 │
      ▼                 ▼
┌─────────────┐  ┌─────────────┐
│ FastAPI API │  │ Fraud Alerts│
│   Serving   │  │     CSV     │
└──────┬──────┘  └──────┬──────┘
       │                │
       ▼                ▼
┌─────────────┐  ┌─────────────┐
│ Swagger UI  │  │ Streamlit   │
│ API Testing │  │ Dashboard   │
└─────────────┘  └──────┬──────┘
                        │
                        ▼
               ┌────────────────┐
               │ Fraud Analytics│
               │ Risk Monitoring│
               │ Alert Tracking │
               └────────────────┘

        ┌────────────────────┐
        │       MLflow       │
        │ Experiment Tracking│
        │ Metrics & Models   │
        └────────────────────┘
```

