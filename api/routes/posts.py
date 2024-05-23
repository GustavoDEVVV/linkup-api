from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.database import get_db

from api.deps import CurrentUser, get_current_active_user
from api.crud.posts import select_posts, insert_post, delete_post, get_post_by_id, update_post
from api.schemas.posts import PostCreate, PostUpdate

router = APIRouter(
    prefix='/users',
    tags=['posts']
)

response = requests.get(self.base_url)
        assert isinstance(response.json(), dict)
        assert response.status_code == 401
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


@router.delete('/{username}/posts/{post_id}', dependencies=[Depends(get_current_active_user)])
async def remove_post(post_id: str, session: Session = Depends(get_db)):
    db_post = get_post_by_id(session=session, post_id=post_id)

    if db_post is None:
        raise HTTPException(status_code=404, detail='Post not found')

    delete_post(session=session, post=db_post)
    return {"message": "Post deleted."}


@router.put('/{username}/posts/{post_id}', dependencies=[Depends(get_current_active_user)])
async def put_post(post_id: str,
                   data: PostUpdate,
                   session: Session = Depends(get_db)
                   ):

    db_post = get_post_by_id(session=session, post_id=post_id)

    if db_post is None:
        raise HTTPException(status_code=404, detail='Post not found')

    db_post = update_post(session=session, post_id=post_id, data=data)

    return db_post
