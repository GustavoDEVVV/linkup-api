from pydantic import BaseModel


class UserBase(BaseModel):
    email: str
    username: str


class UserCreate(UserBase):
    password: str


class UserOutPut(UserBase):
    id: int


class User(UserBase):
    id: int
    disabled: bool = False

    class Config:
        from_attributes = True


class UserInDB(User):
    hashed_password: str


# Criar um usuário no form
# ato User.

# user_data = {
# "id": 4,
# "name": "Mary",
# "joined": "2018-11-30",
# }

# user: User = User(**user_data)
