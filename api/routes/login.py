from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session 
from datetime import timedelta
from fastapi import APIRouter

from core.security import ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token
from api.schemas.token import Token
from api.crud.login import authenticate_user
from core.database import get_db

router = APIRouter(
    tags=['token']
)


@router.post('/token')
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
