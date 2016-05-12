# @acts_as_state_machine
class Cerebrum(object):
    # greeting = State(initial=True)
    # waiting_for_type = State()
    # normal_mode = State()

    # greet = Event(from_states=greeting, to_state=waiting_for_type)
    # add_type = Event(from_states=waiting_for_type, to_state=normal_mode)

    def __init__(self, update):
        self.update = update

    def get_respond(self):
        return "Hi, %s!" % self.update.message.chat.username
