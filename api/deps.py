from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from jose import JWTError, jwt
from typing import Annotated

from core.security import oauth2_scheme, ALGORITHM, SECRET_KEY

from api.schemas.users import User
from api.models.users import UserModel
from api.schemas.token import TokenData
from api.crud.reactions import get_user_by_username
from core.database import get_db


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], session: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('sub')
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception

    user = get_user_by_username(session=session, username=token_data.username)

    if user is None:
        raise credentials_exception
    return user

CurrentUser = Annotated[UserModel, Depends(get_current_user)]


async def get_current_active_user(current_user: Annotated[User, Depends(get_current_user)]):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail='Inactive user')
    return current_user


def get_current_active_superuser(current_user: CurrentUser) -> User:
    if not current_user.is_superuser:
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )
    return current_user
