from sqlalchemy import (
    Column,
    Integer,
    Float,
    String,
)

from sqlalchemy.orm import declarative_base

Base = declarative_base()


class FraudAlert(Base):

    __tablename__ = "fraud_alerts"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    amount = Column(Float)

    merchant_id = Column(Integer)

    hour = Column(Integer)

    risk_score = Column(Float)

    prediction = Column(String(20))