"""
Initial create of all tables
"""
import os

from chat.config import engine

from chat.models.user import User
from chat.models.habit import Habit
from chat.models.success_log import SuccessLog



User.metadata.create_all(engine)
Habit.metadata.create_all(engine)
SuccessLog.metadata.create_all(engine)
