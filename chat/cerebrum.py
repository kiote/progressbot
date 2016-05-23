import os

import chat.config as config
from chat.phrases.ru import request
from chat.phrases.ru import response

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

        # main "command interface"
        if message_text.startswith(request["add"]):
            return response["new habit success"]
        elif message_text.startswith(request["success"]):
            return response["new habit log"]

        return response["greeting"].format(user_name)
