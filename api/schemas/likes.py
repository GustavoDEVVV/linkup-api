from pydantic import BaseModel


class LikeCreate(BaseModel):
    PostId: str
    UserId: str
    reaction: str

    class Config:
        orm_mode = True
