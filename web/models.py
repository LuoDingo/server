from flask_login import UserMixin
from . import db
from datetime import datetime

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))
    memberships = db.relationship('Membership', backref='member')

    def __repr__(self):
        return f"User('{self.id}', '{self.name}', '{self.email}')"

class Chatroom(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    memberships = db.relationship("Membership", lazy=True)

    def __repr__(self):
        return f"Chatroom('{self.id}','{self.name}')"

class Membership(db.Model):
    __table_args__ = (
        db.PrimaryKeyConstraint('chat_id', 'member_id'),
    )
    chat_id = db.Column(db.Integer, db.ForeignKey('chatroom.id'))
    member_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.now)
    text = db.Column(db.String(250))
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    room_id = db.Column(db.Integer, db.ForeignKey('chatroom.id'), nullable=False)

    def __repr__(self):
        return f"Message('{self.id}', '{self.date}', '{self.message}')"