from pydantic import BaseModel


class PostBase(BaseModel):
    title: str
    description: str


class PostCreate(PostBase):
    pass


class Post(PostBase):
    id: int
    owner_username: str

    class Config:
        from_attributes = True
