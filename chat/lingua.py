from .cerebrum import Cerebrum

class Lingua(object):
    def __init__(self, update):
        self.update = update

    def respond(self):
        respond = Cerebrum(self.update).get_respond()
        return respond
