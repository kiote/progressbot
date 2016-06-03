import os
import datetime

import chat.config as config
from chat.phrases.ru import request
from chat.phrases.ru import response

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .models.habit import Habit


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

        # first, we need to check that we have at least one racord at habit table
        # if we don't, need to wait till user add it

        # main "command interface"
        # need some kind of Factory pattern here
        if message_text.startswith(request["add"]):
            # check if we have no active habit yet
            habit = self.session.query(Habit).filter_by(user_id=user_id, active=True).first()
            if habit is None:
                habit = Habit(user_id=user_id,
                              active=True,
                              name=self.get_habit_name(message_text),
                              created_at=datetime.datetime.now(),
                              successful_days=0)
                self.session.add(habit)
                self.session.commit()
                return response["new habit success"]
            else:
                return response["can't create habit"] + habit.name
        elif message_text.startswith(request["success"]):
            # need to check, of we have no success log for the last 20 hours yet
            # if we have not, let's add this log
            return response["new habit log"]

        return response["greeting"].format(user_name)

    def get_habit_name(self, message):
        return "Название привычки"
