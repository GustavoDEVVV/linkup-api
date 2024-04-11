from sqlalchemy import create_engine  # type: ignore
from sqlalchemy.ext.declarative import declarative_base  # type: ignore
from sqlalchemy.orm import sessionmaker, Session  # type: ignore

from core.config import settings  # type: ignore
import uuid

engine = create_engine(
    settings.SQLALCHEMY_DATABASE_URI,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


def get_db():
    database = SessionLocal()
    try:
        yield database
    finally:
        database.close()


def generate_small_uuid() -> str:
    return str(uuid.uuid4())[:8]
