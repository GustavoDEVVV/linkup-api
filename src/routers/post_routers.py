from fastapi import APIRouter
from utils.helpers import get_db

post_router = APIRouter(
    prefix='/posts',
    tags=['posts'],
    responses={400: {'description': 'Not found'}}
)


@post_router.get('/')
async def read_posts():
    return [{"id": 1, "title": "Jonathas", "description": "Gostaria de enfatizar que..."}, {"id": 1, "nome": "Jonathas"},]
