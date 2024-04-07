from sqlalchemy.orm import Session  # type: ignore
from api.schemas.users import UserSchema


def select_user_by_username(session: Session, username: str):
    return session.query(UserSchema).filter(UserSchema.username == username).first()
