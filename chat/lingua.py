class Lingua(object):
    def __init__(self, update):
        self.update = update

    def respond(self):
        return "Hi, %s!" % self.update.message.chat.username
