from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from core.db import Base


class UserModel(Base):
    __tablename__ = 'users'

    id = Column(String(36), primary_key=True)
    slug = Column(String(7))

    username = Column(String(50), unique=True)
    first_name = Column(String(50))
    last_name = Column(String(50))

    email = Column(String(40), unique=True, index=True)
    password = Column(String(40))

    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)

    posts = relationship('PostModel', back_populates='owner')


class PostModel(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(35), index=True)
    description = Column(String(255), index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship('UserModel', back_populates='posts')
