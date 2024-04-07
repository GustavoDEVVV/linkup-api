from core.db import Base


import uuid
from fastapi_utils.guid_type import GUID_DEFAULT_SQLITE, GUID
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from api.deps import generate_small_uuid


from api.validators.post_validators import Post


class UserModel(Base):
    __tablename__ = 'users'

    id = Column(
        GUID,
        primary_key=True,
        default=GUID_DEFAULT_SQLITE
    )

    username = Column(String(50), unique=True)
    first_name = Column(String(50))
    last_name = Column(String(50))

    email = Column(String(40), unique=True, index=True)
    password = Column(String(40))

    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)

    posts: list['Post'] = relationship(
        'PostModel', back_populates='owner')


class PostModel(Base):
    __tablename__ = 'posts'

    id = Column(
        GUID,
        primary_key=True,
        default=GUID_DEFAULT_SQLITE
    )

    slug = Column(
        String(8),
        unique=True,
        default=generate_small_uuid
    )

    title = Column(String(35), index=True)
    description = Column(String(255), index=True)
    owner_username = Column(String(50), ForeignKey("users.username"))

    owner = relationship('UserModel', back_populates='posts')


class LikeModel(Base):
    __tablename__ = 'likes'

    postId = Column(
        GUID,
        ForeignKey("posts.id"),
        primary_key=True
    )

    userId = Column(
        GUID,
        ForeignKey("users.id"),
        primary_key=True
    )
    
    user = relationship('UserModel', backref='likes')
    post = relationship('PostModel', backref='likes')
