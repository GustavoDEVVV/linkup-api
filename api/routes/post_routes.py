from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.validators.post_validators import PostCreate

from core.db import Base, engine
from api.crud.post_crud import select_posts, insert_post
from api.deps import get_db

Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix='/users',
    tags=['posts']
)


@router.get('/{username}/posts/')
async def get_posts(username: str, db: Session = Depends(get_db)):
    posts = select_posts(db, username=username)
    return posts


@router.post('/{username}/posts/')
async def post_post(username: str, post: PostCreate,  db: Session = Depends(get_db)):
    return insert_post(db=db, post=post, username=username)


@router.delete('/{username}/post/')
async def delete_post(username: str, post: PostCreate, db: Session = Depends(get_db)):
    return delete_post(db=db, delete=post, username=username) 