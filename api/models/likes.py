from sqlalchemy import Boolean, Column, ForeignKey, Integer, String  # type: ignore
from sqlalchemy.orm import relationship   # type: ignore
from core.database import Base


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
