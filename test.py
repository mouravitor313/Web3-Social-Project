from flask import Flask, request, render_template
from check_balance import Wallet
from transaction import Transaction

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Cindex.html')

@app.route('/balance', methods=['POST'])
def balance():
    public_id = request.form['public_id']
    wallet = Wallet(public_id)
    balance = wallet.balance()
    return render_template('balance.html', balance=balance)

@app.route('/transaction', methods=['POST'])
def transaction():
    public_id = request.form['public_id']
    private_key = request.form['private_key']
    estrangeira = request.form['estrangeira']
    value = float(request.form['value'])
    wallet = Wallet(public_id)
    balance = wallet.balance()
    if value > balance:
        error = 'Error: Insufficient funds in wallet for transaction.'
        return render_template('transaction.html', error=error)
    else:
        transaction = Transaction(private_key, estrangeira, value)
        transaction.transaction()
        success = 'Transaction successful!'
        return render_template('transaction.html', success=success)

if __name__ == '__main__':
    app.run()
