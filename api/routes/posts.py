from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.database import get_db

from api.deps import get_current_active_superuser, CurrentUser, get_current_active_user
from api.crud.posts import select_posts, insert_post
from api.schemas.posts import PostCreate

router = APIRouter(
    prefix='/users',
    tags=['posts']
)


@router.get('/{username}/posts')
async def read_posts(username: str, session: Session = Depends(get_db)):
    try:
        posts = select_posts(session, username)
        for post in posts:
            post_dict = post.__dict__
            post_dict.pop('id')
            post_dict.pop('owner_username')
        return posts
    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))


@router.post('/{username}/posts', dependencies=[Depends(get_current_active_user)])
async def create_new_post(post: PostCreate, username: str, session: Session = Depends(get_db)):
    try:
        response = insert_post(session=session, post=post, username=username)
        return response
    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))
