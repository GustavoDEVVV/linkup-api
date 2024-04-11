from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.validators.like_validators import LikeCreate
from api.crud.like_crud import create_like, get_likes_by_post_id, delete_like
from api.deps import get_db

router = APIRouter(prefix='/likes', tags=['likes'])


@router.post('/')
async def like_post(like_data: LikeCreate, db: Session = Depends(get_db)):
    try:
        created_like = create_like(db=db, **like_data.dict())
        return created_like
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get('/{post_id}/')
async def get_likes_for_post(post_id: str, db: Session = Depends(get_db)):
    try:
        likes = get_likes_by_post_id(db=db, post_id=post_id)
        return likes
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete('/{post_id}/{user_id}/')
async def unlike_post(post_id: str, user_id: str, db: Session = Depends(get_db)):
    try:
        result = delete_like(db=db, post_id=post_id, user_id=user_id)
        if result:
            return {"message": "Like deleted successfully"}
        else:
            raise HTTPException(status_code=404, detail="Like not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
