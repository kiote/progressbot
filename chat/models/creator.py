"""
Initial create of all tables
"""
import os

import chat.config as config

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


engine = create_engine(os.getenv('DATABASE_URL', config.DATABASE_URL), echo=True)
Base = declarative_base()


class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    event_name = Column(String(120))

    def __repr__(self):
        return "Event user_id=%s, name=%s" % (self.user_id, self.event_name)


Base.metadata.create_all(engine)
