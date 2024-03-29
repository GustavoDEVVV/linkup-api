from fastapi import APIRouter
from core.db import Base, engine

Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix='/posts',
    tags=['posts']
)


@router.get('/')
def read_users():
    return 'rota de posts'
