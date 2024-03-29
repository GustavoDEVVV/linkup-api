from sqlalchemy.orm import Session
from api.models import UserModel
from api.validators.user_validators import UserCreate


def select_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(UserModel).offset(skip).limit(limit).all()


def create_user(db: Session, user: UserCreate):
    db_user = UserModel(
        username=user.username,
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        password=user.password
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return {"message": "User created"}


def select_user_by_email(db: Session, email: str):
    return db.query(UserModel).filter(UserModel.email == email).first()


def select_user_by_username(db: Session, username: str):
    return db.query(UserModel).filter(UserModel.username == username).first()
