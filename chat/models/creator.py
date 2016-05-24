"""
Initial create of all tables
"""
import os

import chat.config as config

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, DateTime, SmallInteger


engine = create_engine(os.getenv('DATABASE_URL', config.DATABASE_URL), echo=True)
Base = declarative_base()


class Habit(Base):
    __tablename__ = 'habits'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    name = Column(String(120))
    active = Column(Boolean)
    created_at = Column(DateTime)
    successful_days = Column(SmallInteger)

    def __repr__(self):
        return "Event user_id=%s, name=%s" % (self.user_id, self.name)


Base.metadata.create_all(engine)
