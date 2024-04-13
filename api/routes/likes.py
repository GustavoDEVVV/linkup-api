from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.schemas.likes import LikeCreate
from api.crud.likes import create_like, get_likes_by_post_id, delete_like
from api.crud.posts import get_post_by_id
from api.crud.users import get_user_by_username
from api.deps import get_db

router = APIRouter(prefix='/posts/{post_id}/likes', tags=['likes'])


@router.post('/')
async def like_post(like_data: LikeCreate, session: Session = Depends(get_db)):
    try:
        user = get_user_by_username(session, user_id=like_data.UserId)
        post = get_post_by_id(session, post_id=like_data.PostId)

        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        if not post:
            raise HTTPException(status_code=404, detail="Post not found")

        
        created_like = create_like(
            session=session, post_id=like_data.PostId, user_id=like_data.UserId, reaction=like_data.reaction)
        return created_like
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get('/')
async def get_likes_for_post(post_id: str, session: Session = Depends(get_db)):
    try:
        post = get_post_by_id(session, post_id=post_id)
        if not post:
            raise HTTPException(status_code=404, detail="Post not found")

        likes = get_likes_by_post_id(session=session, post_id=post_id)
        return likes
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete('/{post_id}/{user_id}/')
async def unlike_post(post_id: str, user_id: str, session: Session = Depends(get_db)):
    try:
        user = get_user_by_username(session, user_id=user_id)
        post = get_post_by_id(session, post_id=post_id)

        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        if not post:
            raise HTTPException(status_code=404, detail="Post not found")

        result = delete_like(session=session, post_id=post_id, user_id=user_id)
        if result:
            return {"message": "Like deleted successfully"}
        else:
            raise HTTPException(status_code=404, detail="Like not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
