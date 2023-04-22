import gino

from tgbot.models import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)
    nickname = db.Column(db.Unicode(), default='noname')
    user_id = db.Column(db.BigInteger)
