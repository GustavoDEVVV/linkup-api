from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from core.database import Base, generate_small_uuid


class PostModel(Base):
    __tablename__ = 'posts'

    id = Column(
        String(8),
        primary_key=True,
        default=generate_small_uuid
    )
    title = Column(String(50))
    description = Column(String(255))
    owner_username = Column(String(50), ForeignKey('users.username'))

    owner = relationship('UserModel', back_populates='posts')
