from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from core.db import Base, engine
from api.crud.user_crud import (
    select_users, create_user,
    select_user_by_username,
    select_user_by_email
)
from api.validators.user_validators import User, UserCreate, UserBase
from api.validators.post_validators import Post
from api.deps import get_db

Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix='/users',
    tags=['users'],
    responses={404: {'description': 'Not found'}}
)


@router.get('/', response_model=list)
async def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    try:
        user_posts = []
        users = select_users(db, skip=skip, limit=limit)
        for user in users:
            user_dict = user.__dict__
            user_dict['posts'] = [post.__dict__ for post in user.posts]

            user_dict.pop('id')
            user_dict.pop('email')
            user_dict.pop('password')

            user_dict.pop('is_admin')
            user_dict.pop('is_active')

            user_posts.append(user_dict)

            for post in user_dict['posts']:
                post.pop('id')
                post.pop('owner_username')

        return user_posts
    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))


@router.post('/')
async def post_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        exceptions = []
        user_exists_email = select_user_by_email(
            db, email=user.email
        )
        user_exists_username = select_user_by_username(
            db, username=user.username
        )
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

    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))