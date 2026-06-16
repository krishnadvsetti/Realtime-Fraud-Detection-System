import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, roc_auc_score
import mlflow
import mlflow.sklearn

from xgboost import XGBClassifier
from imblearn.over_sampling import SMOTE

import joblib


df = pd.read_csv("data/creditcard.csv")

X = df.drop("Class", axis=1)
y = df["Class"]

mlflow.set_experiment("fraud_detection")

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# SMOTE goes here
smote = SMOTE(random_state=42)

X_train_resampled, y_train_resampled = smote.fit_resample(
    X_train,
    y_train
)

# Model
model = XGBClassifier(
    n_estimators=200,
    max_depth=6,
    learning_rate=0.1,
    eval_metric="logloss"
)

# Train on resampled data
model.fit(
    X_train_resampled,
    y_train_resampled
)

preds = model.predict(X_test)

probs = model.predict_proba(X_test)[:, 1]

auc = roc_auc_score(y_test, probs)

print(classification_report(y_test, preds))
print(f"ROC-AUC: {auc:.4f}")

joblib.dump(model, "models/xgboost_model.pkl")

print("Model saved")

with mlflow.start_run():

    mlflow.log_param("model", "xgboost")
    mlflow.log_param("smote", True)

    model.fit(
        X_train_resampled,
        y_train_resampled
    )

    preds = model.predict(X_test)

    probs = model.predict_proba(X_test)[:,1]

    auc = roc_auc_score(y_test, probs)

    mlflow.log_metric("roc_auc", auc)

    mlflow.sklearn.log_model(
        model,
        "fraud_model"
    )