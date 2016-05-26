"""
Initial create of all tables
"""
import os

from chat.config import DATABASE_URL

from sqlalchemy import create_engine

from chat.models.user import create_users_table
from chat.models.habit import create_habits_table
from chat.models.success_log import create_success_log_table

engine = create_engine(os.getenv('DATABASE_URL', DATABASE_URL), echo=True)
create_users_table(engine)
create_habits_table(engine)
create_success_log_table(engine)
