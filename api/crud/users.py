from sqlalchemy.orm import Session  # type: ignore
from api.models.users import UserModel
from api.schemas.users import UserCreate
from core.security import get_password_hash
from fastapi import Depends
from core.database import get_db


def get_user_by_username(username: str, session: Session = Depends(get_db)):
    return session.query(UserModel).filter(UserModel.username == username).first()


def get_user_by_email(email: str, session: Session = Depends(get_db)):
    return session.query(UserModel).filter(UserModel.email == email).first()


def get_user(session: Session, user_id: int):
    return session.query(UserModel).filter(UserModel.id == user_id).first()


def create_user(session: Session, user: UserCreate):
    db_object = UserModel(
        email=user.email,
        username=user.username,
        hashed_password=get_password_hash(user.password)
    )

    session.add(db_object)
    session.commit()
    session.refresh(db_object)

    return db_object
