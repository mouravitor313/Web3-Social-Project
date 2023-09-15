from check_balance import web3, Wallet

class Transaction:
    def __init__(self, sender, private, receiver, value):
        self.sender = sender
        self.private = private
        self.receiver = receiver
        self.value = value
        
    @classmethod
    def transaction(cls):

        # Necessary parameters
        sender_public_key = Wallet.get_sender_public_key()
        sender_private_key = input("\nEnter the sender private key: ")
        receiver_public_key = input("\nEnter the receiver public key address: ")
        value = float(input("\nEnter the transaction value: "))

        nonce = web3.eth.get_transaction_count(sender_public_key)

        # Transaction data
        tx = { 
            'nonce': nonce, 
            'to': receiver_public_key, 
            'value': web3.to_wei(value, 'ether'), 
            'gas': 2000000, 
            'gasPrice': web3.to_wei('50', 'gwei') 
        }

        # Doing the transaction
        signed_tx = web3.eth.account.sign_transaction(tx, sender_private_key)
        
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction).hex()
        print("Transaction Hash:", tx_hash)
        return tx_hash


