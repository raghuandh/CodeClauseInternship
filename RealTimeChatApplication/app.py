from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO, emit, join_room, leave_room
import random
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chat.db'
db = SQLAlchemy(app)
socketio = SocketIO(app)

class Room(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), unique=True, nullable = False)
    password = db.Column(db.String(100), nullable = False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create-room', methods=['POST'])
def create_room():
    room_name = request.form.get('room_name')
    password = request.form.get('password')
    username = request.form.get('username')
    if Room.query.filter_by(name=room_name).first():
        return "Room Already Exists"
    new_room = Room(name=room_name, password=password)
    db.session.add(new_room)
    db.session.commit()
    return redirect(url_for('chat', room_name=room_name, username=username))

@app.route('/join', methods=['POST'])
def join_room_form():
    room_name = request.form.get('room_name')
    password = request.form.get('password')
    username = request.form.get('username')
    room = Room.query.filter_by(name=room_name, password=password).first()
    if room:
        return redirect(url_for('chat', room_name=room_name, username=username))
    else:
        return 'Invalid room name or password!'


@app.route('/chat/<room_name>/<username>')
def chat(room_name, username):
    room = Room.query.filter_by(name=room_name).first()
    
    if room:
        # Render the chat room template with the provided room name and username
        return render_template('chat.html', room_name=room_name, username=username)
    else:
        return 'Room does not exist!'
@socketio.on('join')
def join(message,username):
    room = message['room']
    username = username['username']
    join_room(room)
    emit('message', {'msg': f'{username}  has entered the room.'}, room=room, username=username)

@socketio.on('leave')
def leave(message):
    room = message['room']
    username = message['username']
    leave_room(room)
    emit('message', {'msg': f'{username} has left the room.'}, room=room, username=username)

@socketio.on('message')
def handle_message(message):
    room = message['room']
    #username = username['username']
    emit('message', message, room=room)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    socketio.run(app)
