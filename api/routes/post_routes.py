from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from core.db import Base, engine
from api.validators.post_validators import PostCreate
from api.crud.post_crud import select_posts, insert_post
from api.deps import get_db

Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix='/users',
    tags=['posts']
)


@router.get('/{username}/posts/')
async def get_posts(username: str, db: Session = Depends(get_db)):
    try:
        posts = select_posts(db, username=username)
        for post in posts:
            post_dict = post.__dict__
            post_dict.pop('id')
            post_dict.pop('owner_username')
        return posts

    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))


@router.post('/{username}/posts/')
async def post_post(username: str, post: PostCreate,  db: Session = Depends(get_db)):
    try:
        response = insert_post(db=db, post=post, username=username)
        return response

    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))
