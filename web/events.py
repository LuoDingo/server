from . import socketio
from flask_login import current_user
from .models import Message
from . import db

def messageReceived(methods=['GET','POST']):
    print('message was recieved')

@socketio.on('my event')
def user_online(json, methods=['GET', 'POST']):
    # new_message = Message(author_id=current_user.id, text=json['message'], room_id=json['chat_id'])
    # db.session.add(new_message)
    # db.session.commit()
    if 'data' in json:
        print("user online")
        print(json['data'])
        socketio.emit('my response', {'data':json['data']}, callback=messageReceived)
    else:
        print("typing happened")
        json['user'] = current_user.name
        socketio.emit('my response', json, callback=messageReceived)