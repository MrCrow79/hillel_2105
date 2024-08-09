from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from lessons.lesson_22.alchemy_base import Base


class UserTable(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)  # primary_key = unique, not None
    name = Column(String)
    age = Column(Integer)
