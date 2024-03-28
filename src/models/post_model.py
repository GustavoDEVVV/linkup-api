from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship
from database.connection import Base


users_likes = Table(
    'users_friends', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('typeof', String(5))
)


class PostModel(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(35), index=True)
    description = Column(String(255), index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship('UserModel', back_populates='posts')
    likes = relationship(
        'UserModel',
        primaryjoin=users_likes.c.user_id,
        secondaryjoin=users_likes.c.typeof,
        backref='like_of'
    )
