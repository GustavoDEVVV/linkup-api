from pydantic import BaseModel
from pydantic import BaseModel, validator
from sqlalchemy.orm import Session
from api.models import PostModel, UserModel
from api.crud.posts import get_post_by_id
from api.crud.users import get_user_by_username


class LikeCreate(BaseModel):
    PostId: str
    UserId: str
    reaction: str

    class Config:
        orm_mode = True

    @validator('PostId')
    def validate_post_id_exists(cls, v, values, **kwargs):
        db: Session = kwargs['db']
        post = get_post_by_id(db, v)
        if not post:
            raise ValueError(f"Post with id {v} does not exist")
        return v

    @validator('UserId')
    def validate_user_id_exists(cls, v, values, **kwargs):
        db: Session = kwargs['db']
        user = get_user_by_username(db, v)
        if not user:
            raise ValueError(f"User with id {v} does not exist")
        return v
