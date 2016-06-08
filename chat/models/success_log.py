from init import db


class SuccessLog(db.Model):
    __tablename__ = 'success_log'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    habit_id = db.Column(db.Integer, db.ForeignKey('habits.id'))
    created_at = db.Column(db.DateTime)
