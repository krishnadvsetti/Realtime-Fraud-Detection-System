# Real-Time Fraud Detection System

![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688)
![React](https://img.shields.io/badge/React-Frontend-61DAFB)
![Kafka](https://img.shields.io/badge/Apache_Kafka-Streaming-black)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-336791)
![Docker](https://img.shields.io/badge/Docker-Containerization-2496ED)
![XGBoost](https://img.shields.io/badge/XGBoost-Machine_Learning-orange)
![SHAP](https://img.shields.io/badge/SHAP-Explainable_AI-red)
![MLflow](https://img.shields.io/badge/MLflow-Experiment_Tracking-0194E2)

---

## 📖 Overview

The **Real-Time Fraud Detection System** is an end-to-end Machine Learning application designed to identify fraudulent financial transactions in real time. The system continuously streams transaction data through **Apache Kafka**, performs fraud prediction using an **XGBoost** model, stores prediction results in **PostgreSQL**, and provides live monitoring through a **React dashboard**.

To improve model transparency, the system integrates **SHAP (SHapley Additive Explanations)**, enabling feature-level explanations for every prediction.

---

## ✨ Key Features

* 🚀 Real-time transaction streaming using Apache Kafka
* 🤖 Fraud detection using XGBoost
* 📊 SHAP Explainable AI for prediction interpretation
* ⚡ FastAPI REST API
* 🗄 PostgreSQL database integration
* 📈 Live analytics dashboard built with React
* 📉 Fraud monitoring and visualization
* 📦 Dockerized development environment
* 🧪 MLflow experiment tracking
* ⚙ Environment-based configuration using `.env`
* 📝 Centralized logging and error handling

---

# 🏗 System Architecture

```text
                    +----------------------+
                    | Transaction Generator|
                    +----------+-----------+
                               |
                               ▼
                    +----------------------+
                    |    Apache Kafka      |
                    +----------+-----------+
                               |
                               ▼
                    +----------------------+
                    | Fraud Detection      |
                    | Consumer (XGBoost)   |
                    +----------+-----------+
                               |
                 Prediction + Risk Score
                               |
                               ▼
                    +----------------------+
                    |     PostgreSQL       |
                    +----------+-----------+
                               |
                               ▼
                    +----------------------+
                    |      FastAPI API     |
                    +----------+-----------+
                               |
                               ▼
                    +----------------------+
                    |   React Dashboard    |
                    +----------------------+
```

---

# 🛠 Tech Stack

## Backend

* FastAPI
* SQLAlchemy
* PostgreSQL
* Apache Kafka
* Docker

## Machine Learning

* XGBoost
* Scikit-learn
* Pandas
* NumPy
* SHAP
* MLflow
* Joblib

## Frontend

* React
* Material UI
* Axios
* Chart.js

---

# 📂 Project Structure

```text
Realtime-Fraud-Detection-System/

│
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
├── models/
│
├── notebooks/
│
├── src/
│   ├── api/
│   ├── database/
│   ├── explainability/
│   ├── monitoring/
│   ├── streaming/
│   ├── training/
│   └── utils/
│
├── docker-compose.yml
├── requirements.txt
├── README.md
├── .env.example
└── frontend/.env.example
```

---

# 🤖 Machine Learning Pipeline

1. Data Collection
2. Data Preprocessing
3. Feature Engineering
4. Class Imbalance Handling
5. Model Training (XGBoost)
6. Model Evaluation
7. MLflow Experiment Tracking
8. Model Serialization
9. Real-Time Inference
10. SHAP Explainability

---

# 🌐 REST API Endpoints

| Method | Endpoint         | Description                            |
| ------ | ---------------- | -------------------------------------- |
| GET    | `/`              | Application status                     |
| GET    | `/health`        | API health check                       |
| GET    | `/metrics`       | Fraud detection statistics             |
| GET    | `/transactions`  | Latest transactions                    |
| GET    | `/fraud-summary` | Fraud vs Genuine summary               |
| POST   | `/predict`       | Fraud prediction with SHAP explanation |

---

# 📊 Dashboard Features

The React dashboard provides live monitoring with:

* Total Transactions
* Fraud Alerts
* Fraud Rate
* Average Risk Score
* Fraud Distribution Chart
* Recent Transactions Table

---

# 🧠 Explainable AI using SHAP

The system integrates **SHAP (SHapley Additive Explanations)** to provide transparent and interpretable predictions.

For every prediction, the API returns:

* Fraud Prediction
* Prediction Probability
* Feature Importance Scores
* Top Contributing Features

This enables users to understand why a transaction has been classified as fraudulent.

---

# 🚀 Getting Started

## Clone Repository

```bash
git clone https://github.com/your-username/Realtime-Fraud-Detection-System.git

cd Realtime-Fraud-Detection-System
```

---

## Backend Setup

```bash
python -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

uvicorn src.api.app:app --reload
```

---

## Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

---

## Docker

```bash
docker compose up -d
```

---

# 📈 Monitoring

The project includes:

* Kafka Producer
* Kafka Consumer
* PostgreSQL Storage
* FastAPI Backend
* React Dashboard
* MLflow Experiment Tracking
* SHAP Explainability

---

# 🔮 Future Improvements

* JWT Authentication
* Role-Based Access Control (RBAC)
* WebSocket-based Live Updates
* Cloud Deployment (AWS / Azure / GCP)
* CI/CD Pipeline
* Kubernetes Deployment
* Model Monitoring & Drift Detection

---

