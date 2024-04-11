from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, CheckConstraint
from sqlalchemy.orm import relationship
from core.database import Base
from core.database import generate_small_uuid


class ReactionType(String):
    def __init__(self, *args):
        super(ReactionType, self).__init__(length=10)
        self.reactions = set(args)

    def __check_reaction(self, value):
        return value in self.reactions

    def process_bind_param(self, value):
        if value not in self.reactions:
            raise ValueError(f"Invalid reaction: {value}")
        return value


class LikeModel(Base):
    __tablename__ = 'likes'

    postId = Column(
        String(8),
        ForeignKey("posts.id"),
        primary_key=True
    )

    userId = Column(
        String(8),
        ForeignKey("users.id"),
        primary_key=True
    )

    reaction = Column(
        ReactionType('grr', 'like', 'love', 'wow'),
        CheckConstraint("reaction IN ('grr', 'like', 'love', 'wow')"),
        nullable=False
    )

    user = relationship('UserModel', backref='likes')
    post = relationship('PostModel', backref='likes')
