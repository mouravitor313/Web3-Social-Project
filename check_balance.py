from web3 import Web3

sepolia_url = "https://eth-sepolia.g.alchemy.com/v2/pvpIq7da_oW19Vyvv0lJaQ2XlYQpskIa" # network url

web3 = Web3(Web3.HTTPProvider(sepolia_url)) # variable with a url acessor property

class Wallet:
    def __init__(self):
        self

    # Check connection and block number
    @classmethod
    def network_checker(cls):
        return f"Connected: {web3.is_connected()}\nBlock number: {web3.eth.block_number}"

    # Get the address balance
    @classmethod
    def wallet_balance(cls, address):
            balance = web3.eth.get_balance(address)
            return web3.from_wei(balance, 'ether')
    
    @classmethod
    def get_sender_public_key(cls):
        sender_address = input("\nEnter your public key (address): ")
        return sender_address
    
