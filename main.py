from check_balance import Wallet
from transaction import Transaction

# Check Network
print("Connected:", Wallet.network_checker())

# Transaction
sender_public_key = Wallet.get_sender_public_key()
balance1 = Wallet.wallet_balance(sender_public_key)
print(balance1)
Transaction.transaction()
print("Transação bem sucedida!")
# balance2 = Wallet.wallet_balance(sender_public_key)

# Check transaction state
# if balance1 != balance2:
#     print("Transação bem sucedida!")

