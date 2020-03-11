from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from sqlalchemy import desc
from . import db
from . import events
from .models import Chatroom, Message
import json

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('login.html')

@main.route('/chatroom/<int:chat_id>', methods=['GET'])
@login_required
def chatroom_view(chat_id):
    stuff = Message.query.filter_by(room_id=chat_id).order_by(Message.date).limit(50).all()
    chatroom = Chatroom.query.get(chat_id)
    for item in stuff:
        print(item)
    return render_template('chatroom.html', is_authenticated=current_user.is_authenticated, chat_id=chat_id)

@main.route('/chatroom/create', methods=['POST'])
@login_required
def create_chatroom():
    data = request.get_json()
    new_room = Chatroom(name=data['chat_name'])
    db.session.add(new_room)
    db.session.commit()
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

@main.route('/profile')
@login_required
def profile():
    chatrooms = Chatroom.query.all()
    return render_template('profile.html', name=current_user.name, chatrooms=chatrooms)


