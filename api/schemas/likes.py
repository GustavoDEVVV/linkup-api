from pydantic import BaseModel


class LikeBase(BaseModel):
    userId: str
    reaction: str


class LikeCreate(LikeBase):
    pass


class Like(LikeBase):
    PostId: str

    class Config:
        orm_mode = True
