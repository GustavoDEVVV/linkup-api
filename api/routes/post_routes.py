from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from core.db import Base, engine
from api.crud.post_crud import select_posts
from api.deps import get_db

Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix='/users',
    tags=['posts']
)


@router.get('/{user_id}/posts/')
async def get_posts(user_id: int, db: Session = Depends(get_db)):
    posts = select_posts(db, user_id=user_id)
    return posts
