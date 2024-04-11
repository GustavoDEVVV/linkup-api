from sqlalchemy import Boolean, Column, ForeignKey, Integer, String  # type: ignore
from sqlalchemy.orm import relationship   # type: ignore
from core.database import Base


class PostModel(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    description = Column(String(255))
    owner_username = Column(String(50), ForeignKey('users.username'))

    owner = relationship('UserModel', back_populates='posts')
