from pydantic import BaseModel


class PostBase(BaseModel):
    title: str
    description: str | None = None


class PostCreate(PostBase):
    pass
    # def model_dump(self):
    #     return dict(self)


class Post(PostBase):
    id: int
    owner_username: str

    class Config:
        from_attributes = True
