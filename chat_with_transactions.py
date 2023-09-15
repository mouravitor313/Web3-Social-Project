from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO, send
from check_balance import Wallet
from transaction import Transaction

app = Flask(__name__)
app.config['SECRET'] = 'secret!123'
socketio = SocketIO(app, cors_allowed_origins = '*')

posts = []

@socketio.on('message')
def handle_message(message):
    print('Received message: ' + message)
    if message.startswith('balance:'):
        public_id = message.split(':')[1]
        wallet = Wallet()
        balance = wallet.wallet_balance(public_id)
        send(f'Balance: {balance}', broadcast=True)
    elif message.startswith('transaction:'):
        public_id, private_key, foreign_key, value = message.split(':')[1:]
        value = float(value)
        wallet = Wallet()
        balance = wallet.wallet_balance(public_id)
        if value > balance:
            send('Error: Insufficient funds in wallet for transaction.', broadcast=True)
        else:
            transaction = Transaction(public_id,private_key, foreign_key, value)
            tx_hash = transaction.transaction()
            send(f'Transaction successful! Transaction Hash: {tx_hash}', broadcast=True)
    else:
        send(message, broadcast=True)


@app.route('/')
def index():
    return render_template("Cindex.html")

@app.route('/post', methods=['POST'])
def post():
    content = request.form['content']
    if len(content) <= 280:  # Limite de caracteres do Twitter
        posts.append(content)
    return redirect(url_for('get_posts'))


@app.route('/posts')
def get_posts():
    return render_template('posts.html', posts=posts)

if __name__ == '__main__':
    socketio.run(app, host='localhost')

if __name__ == '__main__':
    socketio.run(app, host='localhost')
