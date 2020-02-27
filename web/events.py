from . import socketio
from flask_login import current_user

def messageReceived(methods=['GET','POST']):
    print('message was recieved')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    json['user'] = current_user.name
    socketio.emit('my response', json, callback=messageReceived)