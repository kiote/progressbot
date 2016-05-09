from flask_sqlalchemy import SQLAlchemy


class Memoriae(Object):
    def __init__(self, app):
        self.app = app
