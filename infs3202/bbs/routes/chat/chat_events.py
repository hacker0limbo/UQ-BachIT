from flask_socketio import (
    SocketIO,
    emit,
    join_room,
    leave_room,
)
from flask import session


socketio = SocketIO()


@socketio.on('joined', namespace='/chat')
def joined(message):
    """当客户端进入一个房间, 会向服务端发送一个消息,
    然后 status 消息向所有在这个房间的人广播"""
    room = message['msg']
    join_room(room)
    session['room'] = room
    emit('status', {'msg': session.get('name') + ' has entered the room.'}, room=room)


@socketio.on('text', namespace='/chat')
def text(message):
    """当客户端一个用户发送了一条消息以后触发, 服务端将消息广播给所有在该房间的人"""
    print('room', session.get('room'))
    room = message.get('room')
    emit('message', {'msg': '👤' + session.get('name') + ': ' + message['msg']}, room=room)


@socketio.on('left', namespace='/chat')
def left(message):
    """当客户端某个用户离开, 服务端将离开消息广播给所有用户"""
    room = session.get('room')
    session.pop('room')
    leave_room(room)
    emit('status', {'msg': session.get('name') + ' has left the room.'}, room=room)


