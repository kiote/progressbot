from sqlalchemy.orm import relationship

from init import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    created_at = db.Column(db.DateTime)

    habits = relationship("Habit")
