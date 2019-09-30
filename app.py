from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ekisde'
app.config['DEBUG'] = True
socketio = SocketIO(app)



@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('message')
def chat(msg):
    print('USUARIO: '+ msg)
    send(msg, broadcast = True)


if __name__ == '__main__':
    socketio.run(app)