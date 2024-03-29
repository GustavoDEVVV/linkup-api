from sqlalchemy.orm import Session
from api.models import UserModel


def select_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(UserModel).offset(skip).limit(limit).all()
