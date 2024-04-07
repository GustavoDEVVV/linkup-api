from fastapi import APIRouter
from api.schemas.users import UserSchema

router = APIRouter()


@router.get('/')
def read_root():
    return {"hello": "world"}


@router.get('/users/{item_id}')
def read_user(item_id: int):
    return {"item_id": item_id, }


@router.put('/users/{item_id}')
def update_user(item_id: int, item: UserSchema):
    return {
        "item_name": item.name,
        "item_id": item_id
    }
