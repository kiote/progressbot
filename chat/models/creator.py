"""
Initial create of all tables
"""
import os

from chat.config import DATABASE_URL

from sqlalchemy import create_engine

from chat.models.user import User
from chat.models.habit import Habit
from chat.models.success_log import SuccessLog

engine = create_engine(os.getenv('DATABASE_URL', DATABASE_URL), echo=True)
User.metadata.create_all(engine)
Habit.metadata.create_all(engine)
SuccessLog.metadata.create_all(engine)
