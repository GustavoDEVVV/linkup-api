from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.database import get_db

from api.deps import get_current_active_superuser, CurrentUser, get_current_active_user
from api.crud.posts import select_posts, insert_post, delete_post, get_post_by_id
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
async def create_new_post(post: PostCreate, current_user: CurrentUser, session: Session = Depends(get_db)):
    try:
        username = current_user.username
        response = insert_post(session=session, post=post, username=username)
        return response
    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))


@router.delete('/{username}/post/{post_id}', dependencies=[Depends(get_current_active_user)])
async def remove_post(post_id: str, session: Session = Depends(get_db)):
    db_post = get_post_by_id(session=session, post_id=post_id)

    if db_post is None:
        raise HTTPException(status_code=404, detail='Post not found')

    delete_post(session=session, post=db_post)
    return {"message": f"Post deleted."}
