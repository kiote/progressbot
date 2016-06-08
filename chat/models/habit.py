from sqlalchemy.orm import relationship

from chat.models.success_log import SuccessLog

from init import db


class Habit(db.Model):
    __tablename__ = 'habits'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    name = db.Column(db.String(120))
    active = db.Column(db.Boolean)
    created_at = db.Column(db.DateTime)
    successful_days = db.Column(db.SmallInteger)

    success_log = relationship(SuccessLog)

    def __repr__(self):
        return "Event user_id=%s, name=%s" % (self.user_id, self.name)
