from fastapi import APIRouter
from utils.helpers import get_db

from src.validators.user_validators import UserValidator, UserCreateValidator
# from validators.user_validators import UserValidator, UserCreateValidator

user_router = APIRouter(
    prefix='/users',
    tags=['users'],
    responses={400: {'description': 'Not found'}}
)


@user_router.get('/', response_model=list[UserValidator])
async def read_users():
    return [{"id": 1, "nome": "Exemplo1"}, {"id": 2, "nome": "Exemplo2"},]
