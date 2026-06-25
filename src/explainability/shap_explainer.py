import joblib
import pandas as pd
import shap

from src.utils.config import MODEL_PATH


class FraudExplainer:

    def __init__(self):

        self.model = joblib.load(MODEL_PATH)

        self.explainer = shap.TreeExplainer(
            self.model
        )

    def explain(self, transaction: dict):

        features = pd.DataFrame(
            [[
                transaction["amount"],
                transaction["merchant_id"],
                transaction["hour"]
            ]],
            columns=[
                "amount",
                "merchant_id",
                "hour"
            ]
        )

        prediction = self.model.predict(features)[0]

        probability = float(
            self.model.predict_proba(features)[0][1]
        )

        shap_values = self.explainer.shap_values(
            features
        )

        if isinstance(shap_values, list):
            values = shap_values[1][0]
        else:
            values = shap_values[0]

        explanation = []

        for feature, impact in zip(
            features.columns,
            values
        ):

            explanation.append(
                {
                    "feature": feature,
                    "value": float(features.iloc[0][feature]),
                    "impact": round(float(impact), 4)
                }
            )

        explanation.sort(
            key=lambda x: abs(x["impact"]),
            reverse=True
        )

        return {

            "prediction":
                "FRAUD"
                if prediction == 1
                else "GENUINE",

            "probability":
                round(probability * 100, 2),

            "top_features":
                explanation
        }


explainer = FraudExplainer()