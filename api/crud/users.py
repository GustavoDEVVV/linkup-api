from sqlalchemy.orm import Session  # type: ignore
from api.models.users import UserModel
from api.schemas.users import UserCreate, UserUpdateMe, UserCreateSuperUser
from core.security import get_password_hash
from fastapi import Depends, HTTPException
from core.database import get_db


def get_user_by_username(username: str, session: Session = Depends(get_db)):
    return session.query(UserModel).filter(UserModel.username == username).first()


def get_user_by_email(session: Session, email: str):
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


def select_users(session: Session, skip: int = 0, limit: int = 100):
    return session.query(UserModel).offset(skip).limit(limit).all()


def create_super_user(session: Session, user: UserCreateSuperUser):
    db_object = UserModel(
        email=user.email,
        is_superuser=True,
        username=user.username,
        hashed_password=get_password_hash(user.password)
    )

    session.add(db_object)
    session.commit()
    session.refresh(db_object)

    return db_object


# def update_user(session: Session, user: UserUpdateMe):
#     existing_user = get_user_by_email(session, user.email)

#     if existing_user and existing_user.id != user.id:
#         raise HTTPException(status_code=400, detail="Email already in use")

#     db_user = session.query(UserModel).filter(
#         UserModel.username == user.username).first()

#     if db_user:
#         db_user.email = user.email
#         db_user.username = user.username

#         session.commit()
#         session.refresh(db_user)

#     return db_user
