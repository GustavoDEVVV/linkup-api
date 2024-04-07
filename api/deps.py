from core.database import SessionLocal
from sqlalchemy.orm import Session  # type: ignore
from typing import Annotated


def get_db():
    database = SessionLocal()
    try:
        yield database
    finally:
        database.close()


SessionDep = Annotated[Session, get_db]
