from pydantic import BaseModel


class PostValidatorBase(BaseModel):
    title: str
    description: str | None = None


class PostValidatorCreate(BaseModel):
    pass


class PostValidator(PostValidatorBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True
