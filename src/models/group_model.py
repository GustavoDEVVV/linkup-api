from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship
from database.connection import Base


class GroupModel(Base):
    __tablename__ = 'groups'
    
    