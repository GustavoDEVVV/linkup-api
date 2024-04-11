from sqlalchemy import Boolean, Column, ForeignKey, Integer, String  # type: ignore
from sqlalchemy.orm import relationship   # type: ignore

from core.database import Base
from api.schemas.posts import Post


class UserModel(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)

    username = Column(String(50), unique=True)
    email = Column(String(50), unique=True)
    hashed_password = Column(String(100))

    disabled = Column(Boolean, default=False)
    is_superuser = Column(Boolean, default=False)
    posts = relationship(
        'PostModel', back_populates='owner')
