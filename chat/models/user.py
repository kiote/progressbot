from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, DateTime

from .habit import Habit

Base = declarative_base()


def create_users_table(engine):
    Base.metadata.create_all(engine)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    created_at = Column(DateTime)

    habits = relationship(Habit)
