from pydantic import BaseModel, EmailStr
from src.validators.post_validators import PostValidator


class UserBaseValidator(BaseModel):
    email: EmailStr


class UserCreateValidator(UserBaseValidator):
    password: str


class UserValidator(UserBaseValidator):
    id: int = None
    posts: list[PostValidator] = []
    groups: list[PostValidator] = []
    friends: list[PostValidator] = []

    class Config:
        from_attributes = True
