from pydantic import BaseModel


class PostBase(BaseModel):
    title: str
    description: str | None = None


class PostUpdate(PostBase):
    pass


class PostCreate(PostBase):
    pass


class Post(PostBase):
    id: str
    owner_username: str

    class Config:
        from_attributes = True
