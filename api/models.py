from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from core.db import Base
from fastapi_utils.guid_type import GUID, GUID_DEFAULT_SQLITE


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

    posts = relationship('PostModel', back_populates='owner')


class PostModel(Base):
    __tablename__ = 'posts'

    id = Column(
        GUID,
        primary_key=True,
        default=GUID_DEFAULT_SQLITE
    )
    title = Column(String(35), index=True)
    description = Column(String(255), index=True)
    owner_username = Column(String(50), ForeignKey("users.username"))

    owner = relationship('UserModel', back_populates='posts')
