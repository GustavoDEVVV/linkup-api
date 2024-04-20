from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta
from fastapi import APIRouter

from core.security import ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token
from api.schemas.token import Token
from api.crud.login import authenticate_user, get_user_by_username
from api.crud.users import create_user
from core.database import get_db
from api.schemas.users import UserCreate, UserOutPut
from core.config import settings


router = APIRouter(
    tags=['auth']
)


@router.post('/login')
async def login_for_access_token(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()], session: Session = Depends(get_db)) -> Token:
    user = authenticate_user(session, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={'sub': user.username},  expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type='bearer')


@router.post('/signup', response_model=UserOutPut)
async def register_user(user_in: UserCreate, session: Session = Depends(get_db)):

    if not settings.USERS_OPEN_REGISTRATION:
        raise HTTPException(
            status_code=403,
            detail="Open user registration is forbidden on this server",
        )

    user = get_user_by_username(session=session, username=user_in.username)

    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this email already exists in the system",
        )

    user = create_user(session, user_in)

    user_response = UserOutPut(
        id=user.id,
        username=user.username,
        email=user.email,
    )

    return user_response
