from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, DateTime

from chat.config import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    created_at = Column(DateTime)

    habits = relationship("Habit")
