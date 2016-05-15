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


class Dialog(Base):
    __tablename__ = 'dialogs'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    step = Column(String(120))

    def __repr__(self):
        return "Dialog user_id=%s, step=%s" % (self.user_id, self.step)


Base.metadata.create_all(engine)
