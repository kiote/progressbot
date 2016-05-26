from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, DateTime, ForeignKey


Base = declarative_base()


def create_success_log_table(engine):
    Base.metadata.create_all(engine)


class SuccessLog(Base):
    __tablename__ = 'success_log'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    habit_id = Column(Integer, ForeignKey('habits.id'))
    created_at = Column(DateTime)
