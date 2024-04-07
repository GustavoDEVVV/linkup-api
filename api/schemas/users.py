from pydantic import BaseModel


class UserSchema(BaseModel):
    id: int
    username: str
    email: str
    full_name: str | None = None
    disabled: bool | None = None

    class Config:
        orm_mode = True

# Criar um usuário no formato User.

# user_data = {
# "id": 4,
# "name": "Mary",
# "joined": "2018-11-30",
# }

# user: User = User(**user_data)
