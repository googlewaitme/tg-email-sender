import gino

from tgbot.models import db


class Channel(db.Model):
    __tablename__ = 'channels'
    id = db.Column(db.Integer, primary_key=True)
    unique_id = db.Column(db.BigInteger)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    _user = None

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, value):
        self._user = value
