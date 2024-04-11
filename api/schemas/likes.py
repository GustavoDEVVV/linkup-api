from pydantic import BaseModel


class LikeCreate(BaseModel):
    PostId: str
    UserId: str

    class Config:
        orm_mode = True
