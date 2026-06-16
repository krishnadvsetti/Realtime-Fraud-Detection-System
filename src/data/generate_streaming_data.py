import pandas as pd
import random

rows = []

for _ in range(50000):

    amount = round(random.uniform(1, 5000), 2)
    merchant_id = random.randint(1, 100)
    hour = random.randint(0, 23)

    fraud_score = 0

    if amount > 4000:
        fraud_score += 1

    if hour < 5:
        fraud_score += 1

    if merchant_id > 90:
        fraud_score += 1

    if fraud_score >= 2:
        is_fraud = 1
    else:
        is_fraud = 1 if random.random() < 0.02 else 0

    rows.append([
        amount,
        merchant_id,
        hour,
        is_fraud
    ])

df = pd.DataFrame(
    rows,
    columns=[
        "amount",
        "merchant_id",
        "hour",
        "is_fraud"
    ]
)

df.to_csv(
    "data/streaming_fraud_data.csv",
    index=False
)

print(df.head())
print(df["is_fraud"].value_counts())