import os

import chat.config as config

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class Cerebrum(object):

    def __init__(self, update):
        self.update = update.to_dict()
        engine = create_engine(os.getenv('DATABASE_URL', config.DATABASE_URL), echo=True)
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def get_respond(self):
        user_id = self.update['message']['from']['id']
        user_name = self.update['message']['from']['username']
        message_text = self.update['message']['text'].lower()

        if message_text.startswith('add'):
            return 'Done, new type had been added.'
        elif message_text.startswith('log'):
            return 'Done, log for event had been added.'

        return "Hi, %s!" % user_name
