from pydantic import BaseModel
from api.schemas.posts import Post

from api.schemas.posts import Post


class UserBase(BaseModel):
    email: str
    username: str


class UserCreateSuperUser(UserBase):
    password: str
    is_superuser: bool


class UserUpdateMe(UserBase):
    pass


class UserCreate(UserBase):
    password: str


class UserOutPut(UserBase):
    id: str


class User(UserBase):
    id: str
    disabled: bool = False
    is_superuser: bool = False
    posts: list[Post]

    class Config:
        from_attributes = True


class UserInDB(User):
    hashed_password: str

    class Config:
        from_attributes = True
