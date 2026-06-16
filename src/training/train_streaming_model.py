import pandas as pd
import joblib
import mlflow
import mlflow.sklearn

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    classification_report,
    accuracy_score,
    precision_score,
    recall_score,
    roc_auc_score
)

from xgboost import XGBClassifier


# Create MLflow Experiment
mlflow.set_experiment("streaming_fraud_detection")


# Load Dataset
df = pd.read_csv(
    "data/streaming_fraud_data.csv"
)

X = df[
    [
        "amount",
        "merchant_id",
        "hour"
    ]
]

y = df["is_fraud"]


# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# MLflow Tracking
with mlflow.start_run():

    # Log Parameters
    mlflow.log_param(
        "model",
        "XGBoost"
    )

    mlflow.log_param(
        "n_estimators",
        100
    )

    mlflow.log_param(
        "max_depth",
        4
    )

    mlflow.log_param(
        "learning_rate",
        0.1
    )

    # Model
    model = XGBClassifier(
        n_estimators=100,
        max_depth=4,
        learning_rate=0.1,
        eval_metric="logloss"
    )

    model.fit(
        X_train,
        y_train
    )

    # Predictions
    preds = model.predict(X_test)

    probs = model.predict_proba(X_test)[:, 1]

    # Metrics
    accuracy = accuracy_score(
        y_test,
        preds
    )

    precision = precision_score(
        y_test,
        preds
    )

    recall = recall_score(
        y_test,
        preds
    )

    roc_auc = roc_auc_score(
        y_test,
        probs
    )

    # Log Metrics
    mlflow.log_metric(
        "accuracy",
        accuracy
    )

    mlflow.log_metric(
        "precision",
        precision
    )

    mlflow.log_metric(
        "recall",
        recall
    )

    mlflow.log_metric(
        "roc_auc",
        roc_auc
    )

    # Save Model
    joblib.dump(
        model,
        "models/streaming_fraud_model.pkl"
    )

    # Log Model to MLflow
    mlflow.sklearn.log_model(
        model,
        "fraud_model"
    )

    print(
        classification_report(
            y_test,
            preds
        )
    )

    print(f"Accuracy  : {accuracy:.4f}")
    print(f"Precision : {precision:.4f}")
    print(f"Recall    : {recall:.4f}")
    print(f"ROC-AUC   : {roc_auc:.4f}")

    print(
        "\nStreaming model saved"
    )