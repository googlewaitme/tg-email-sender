import gino

from tgbot.models import db


class Email(db.Model):
    __tablename__ = 'emails'
    id = db.Column(db.Integer(), primary_key=True)
    address = db.Column(db.String(320))
    channel_id = db.Column(db.Integer, db.ForeignKey('channels.id'))
    _channel = None

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
