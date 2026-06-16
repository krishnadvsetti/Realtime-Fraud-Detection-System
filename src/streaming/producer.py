from kafka import KafkaProducer

import json
import random
import time


producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda x:
        json.dumps(x).encode('utf-8')
)


while True:

    transaction = {
        "amount": round(random.uniform(1, 5000), 2),
        "merchant_id": random.randint(1, 100),
        "hour": random.randint(0, 23)
    }

    producer.send(
        "transactions",
        transaction
    )

    print("Sent:", transaction)

    time.sleep(2)