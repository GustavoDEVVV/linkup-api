from sqlalchemy.orm import Session
from api.crud.users import get_user_by_username
from core.security import verify_password


def authenticate_user(username: str, password: str, session: Session):
    user = get_user_by_username(session, username)

    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user
