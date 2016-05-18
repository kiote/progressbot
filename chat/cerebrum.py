import os

import chat.config as config

from state_machine import acts_as_state_machine
from state_machine import State
from state_machine import Event

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .models.creator import Dialog

@acts_as_state_machine
class Cerebrum(object):
    greeting = State(initial=True)
    waiting_for_type = State()
    normal_mode = State()

    greet = Event(from_states=greeting, to_state=waiting_for_type)
    add_type = Event(from_states=waiting_for_type, to_state=normal_mode)

    def __init__(self, update):
        self.update = update.to_dict()
        engine = create_engine(os.getenv('DATABASE_URL', config.DATABASE_URL), echo=True)
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def get_respond(self):
        user_id = self.update['message']['from']['id']
        user_name = self.update['message']['from']['username']
        message_text = self.update['message']['text'].lower()
        dialog = self.session.query(Dialog).filter_by(user_id=user_id).first()

        if dialog is None:
            dialog = Dialog(user_id=user_id, step=self.current_state)
            self.session.add(dialog)
            self.session.commit()

        if message_text.startswith('add'):
            return 'Done, new type had been added.'

        return "Hi, %s!" % user_name
