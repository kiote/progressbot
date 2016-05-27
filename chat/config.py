import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


travis = os.getenv('BUILD_ON_TRAVIS', False)
testing = os.getenv('TESTING', False)

if travis:
    DATABASE_URL = 'postgresql://postgres:@127.0.0.1:5432/progressbot_test'
elif testing:
    DATABASE_URL = 'postgresql://progressbot_test:123456@localhost:5432/progressbot_test'
else:
    DATABASE_URL = 'postgresql://progressbot:123456@localhost:5432/progressbot'

engine = create_engine(os.getenv('DATABASE_URL', DATABASE_URL), echo=True)
Base = declarative_base(bind=engine)
