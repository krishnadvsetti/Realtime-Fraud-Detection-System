import json
import random
import time

from kafka import KafkaProducer
from kafka.errors import KafkaError

from src.utils.config import (
    KAFKA_BOOTSTRAP_SERVERS,
    KAFKA_TOPIC
)
from src.utils.logger import logger


producer = KafkaProducer(
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    value_serializer=lambda x: json.dumps(x).encode("utf-8")
)

logger.info("Kafka Producer Started")


try:

    while True:

        transaction = {
            "amount": round(random.uniform(1, 5000), 2),
            "merchant_id": random.randint(1, 100),
            "hour": random.randint(0, 23)
        }

        producer.send(
            KAFKA_TOPIC,
            transaction
        )

        producer.flush()

        logger.info(f"Transaction Sent: {transaction}")

        time.sleep(2)

except KeyboardInterrupt:

    logger.info("Kafka Producer Stopped")

except KafkaError as e:

    logger.exception(e)

finally:

    producer.close()