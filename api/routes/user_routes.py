from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from core.db import Base, engine
from api.crud.user_crud import (
    select_users, create_user,
    select_user_by_username,
    select_user_by_email
)
from api.validators.user_validators import UserCreate
from api.deps import get_db

Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix='/users',
    tags=['users']
)


@router.get('/')
async def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = select_users(db, skip=skip, limit=limit)
    return users


@router.post('/')
async def post_user(user: UserCreate, db: Session = Depends(get_db)):
    exceptions = []

    user_exists_email = select_user_by_email(db, email=user.email)
    user_exists_username = select_user_by_username(db, username=user.username)

    if user_exists_email:
        exceptions.append("Email already registered")

    if user_exists_username:
        exceptions.append("Username already registered")

    if len(exceptions) > 1:
        raise HTTPException(status_code=400, detail=exceptions)
    elif len(exceptions) == 1:
        raise HTTPException(status_code=400, detail=exceptions[0])
    else:
        return create_user(db=db, user=user)
#
