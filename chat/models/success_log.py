from sqlalchemy import Column, Integer, DateTime, ForeignKey

from chat.config import Base


class SuccessLog(Base):
    __tablename__ = 'success_log'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    habit_id = Column(Integer, ForeignKey('habits.id'))
    created_at = Column(DateTime)
