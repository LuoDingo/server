from flask_login import UserMixin
from . import db
from db import ForeignKey, Integer, Column, String, Model
from db.orm import relationship

class User(UserMixin, Model):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(100), unique=True)
    password = Column(String(100))
    name = Column(String(100))

class ChatRoom(Model):
    __tablename__ = 'chatroom'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    memberships = relationship("Membership")

class Membership(Model):
    __tablename__ = 'membership'
    chat_id = Column(Integer, ForeignKey('chatroom.id'))
    user_id = Column(Integer, ForeignKey('user.id'))

class Message(Model):
    __tablename__ = 'message'

    timestamp = Column()
    chat_message_id
    chat_message_parent_id
    author_id
    room_id


