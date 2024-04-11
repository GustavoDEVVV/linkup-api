from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session  # type: ignore
from api.schemas.likes import LikeCreate
from api.crud.likes import create_like, get_likes_by_post_id, delete_like
from api.deps import get_db

router = APIRouter(prefix='/likes', tags=['likes'])


@router.post('/')
async def like_post(like_data: LikeCreate, session: Session = Depends(get_db)):
    try:
        created_like = create_like(
            session=session, post_id=like_data.PostId, user_id=like_data.UserId, reaction=like_data.reaction)
        return created_like
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get('/{post_id}/')
async def get_likes_for_post(post_id: str, session: Session = Depends(get_db)):
    try:
        likes = get_likes_by_post_id(session=session, post_id=post_id)
        return likes
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete('/{post_id}/{user_id}/')
async def unlike_post(post_id: str, user_id: str, session: Session = Depends(get_db)):
    try:
        result = delete_like(session=session, post_id=post_id, user_id=user_id)
        if result:
            return {"message": "Like deleted successfully"}
        else:
            raise HTTPException(status_code=404, detail="Like not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
