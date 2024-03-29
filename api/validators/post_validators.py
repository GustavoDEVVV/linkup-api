from pydantic import BaseModel


class PostBase(BaseModel):
    title: str
    description: str | None = None


class PostCreate(PostBase):
    def model_dump(self):
        return dict(self)


class Post(PostBase):
    id: str
    owner_username: str

    class Config:
        from_attributes = True
