from src.utils.database import engine
from src.database.models import Base

Base.metadata.create_all(
    bind=engine
)

print("Database tables created")