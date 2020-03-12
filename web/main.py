from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from . import db
from . import events
from .models import Chatroom, Message, User
import json

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('login.html')

@main.route('/chatroom/<int:chat_id>', methods=['GET'])
@login_required
def chatroom_view(chat_id):
    chatroom = Chatroom.query.get(chat_id)
    
    return render_template('chatroom.html', is_authenticated=current_user.is_authenticated, chat_id=chat_id)

@main.route('/chatroom/history/<int:chat_id>')
@login_required
def get_latest(chat_id):
    # history = Message.query.join(User, Message.author_id == User.id).filter_by(room_id=chat_id).order_by(Message.date).limit(50).all()

    # for item in history:
    #     print(item.name)

    things = db.session.query(Message, User).join(Message).filter_by(room_id=chat_id).order_by(Message.date).limit(50).all()
    processed = []
    for item in things:
        processed.append({'date':item[0].date, 'message':item[0].text, 'user':item[1].name})

    for thing in processed:
        print(thing)

    return jsonify(processed)

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