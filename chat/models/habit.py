from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from sqlalchemy import Boolean, DateTime, SmallInteger, ForeignKey

from .success_log import SuccessLog

from chat.config import Base


class Habit(Base):
    __tablename__ = 'habits'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    internal_user_id = Column(Integer, ForeignKey('users.id'))
    name = Column(String(120))
    active = Column(Boolean)
    created_at = Column(DateTime)
    successful_days = Column(SmallInteger)

    success_log = relationship(SuccessLog)

    def __repr__(self):
        return "Event user_id=%s, name=%s" % (self.user_id, self.name)
