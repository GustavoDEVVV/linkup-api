from pydantic import BaseModel


class ReactionBase(BaseModel):
    userId: str
    reaction: str


class ReactionCreate(ReactionBase):
    pass


class ReactionUpdate(BaseModel):
    reaction: str


class Reaction(ReactionBase):
    PostId: str

    class Config:
        orm_mode = True
