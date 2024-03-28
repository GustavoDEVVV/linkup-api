from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship
from database.connection import Base


users_friends = Table(
    'users_friends', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('friend_id', Integer, ForeignKey('users.id'))
)


class UserModel(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, index=True)

    first_name = Column(String(50))
    last_name = Column(String(50))

    email = Column(String(50))
    hashed_password = Column(String(100))

    posts = relationship('PostModel', back_populates='owner')
    groups = relationship('GroupModel', back_populates='member')

    friends = relationship(
        'UserModel',
        primaryjoin=users_friends.c.user_id,
        secondary=users_friends.c.friend_id,
        backref='friend_of'
    )
