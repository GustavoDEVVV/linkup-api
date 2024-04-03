from core.db import SessionLocal
import uuid


def get_db():
    database = SessionLocal()
    try:
        yield database
    finally:
        database.close()


def generate_small_uuid() -> str:
    return str(uuid.uuid4())[:8]
