from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from core.db import Base, engine
from api.crud.user_crud import select_users
from api.deps import get_db

Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix='/users',
    tags=['users']
)


@router.get('/')
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = select_users(db, skip=skip, limit=limit)
    return users
