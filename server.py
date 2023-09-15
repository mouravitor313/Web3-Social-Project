from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET'] = 'secret!123'
socketio = SocketIO(app, cors_allowed_origins = '*')

@socketio.on('message')
def handle_message(message):
    print('Received message: ' + message)
    if message != 'User connected!':
        send(message, broadcast = True)


@app.route('/')
def index():
    return render_template("Cindex.html")

if __name__ == '__main__':
    socketio.run(app, host = 'localhost')

"""
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 9999))
server.listen()

client, addr = server.accept()

done = False

while not done:
    msg = client.recv(1024).decode('utf-8')
    if msg == 'quit':
        done = True
    else:
        print(msg)
    client.send(input("Message: ").encode('utf-8'))
"""