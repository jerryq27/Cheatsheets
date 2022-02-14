from solcx import compile_standard, install_solc
import json
import os
from dotenv import load_dotenv
from web3 import Web3

with open("SimpleStorage.sol", "r") as sol_file:
    simple_storage_sol = sol_file.read()

# Compile the Solidity file.
install_solc("0.6.0")
compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": simple_storage_sol}},
        "settings": {
            "outputSelection": {
                "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
            }
        },
    },
    solc_version="0.6.0",
)

with open("compiled_code.json", "w") as json_file:
    json.dump(compiled_sol, json_file)

# Get the bytecode by traversing the JSON tree.
bytecode = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"][
    "bytecode"
]["object"]

# Get the ABI.
abi = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]

# Deploy to a blockchain VM like Ginache which simulates a blockchain locally with you as the only node.

# RPC Server value in Ganache
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
chain_id = 1337
address = "0x90F8bf6A479f320ead074411a4B0e7944Ea8c9C1"

# Using private keys in Python, you must prepend the '0x'.
# private_key = "0x" + "24d5640bac3b8d9e55520e272058dac69590bd83f50c5f451c9962e1226b4145"
# Instead of using hardcoded private keys, a better approach would be to use environment variables or .env files.

# Environment Variable
# private_key = os.getenv("PRIVATE_KEY")

# .env file.
load_dotenv()
private_key = os.getenv("PRIVATE_KEY")

# Actual deployment.

# Create the contract in Python
SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)

# Get latest transaction using the transaction counter AKA the Nonce
nonce = w3.eth.getTransactionCount(address)

# 1. Build the transaction
transaction = SimpleStorage.constructor().buildTransaction(
    {"chainId": chain_id, "from": address, "nonce": nonce}
)
# 2. Sign the transaction
signed_transaction = w3.eth.account.sign_transaction(
    transaction, private_key=private_key
)

# 3. Send the transaction
transaction_hash = w3.eth.send_raw_transaction(signed_transaction.rawTransaction)

transaction_receipt = w3.eth.wait_for_transaction_receipt(
    transaction_hash=transaction_hash
)

# Working with a contract (Need two things)
# 1. Contract address
# 2. Contract ABI

simple_storage = w3.eth.contract(address=transaction_receipt.contractAddress, abi=abi)

# print(simple_storage.functions.retrieve())
# Call: Simulate making the call and getting a return value.
# Transaction: Actually make a state change.
# print(simple_storage.functions.retrieve().call()) # 0
# print(simple_storage.functions.store(27).call()) # 15
# print(simple_storage.functions.retrieve().call()) # 0 Why? Cause call() is just a simulation.

# Increment Nonce since it is currently pointing to the contract creation transaction.
store_transaction = simple_storage.functions.store(27).buildTransaction(
    {"chainId": chain_id, "from": address, "nonce": nonce + 1}
)
signed_store_transaction = w3.eth.account.sign_transaction(
    store_transaction, private_key=private_key
)
send_store_transaction_hash = w3.eth.send_raw_transaction(
    signed_store_transaction.rawTransaction
)
transaction_receipt = w3.eth.wait_for_transaction_receipt(send_store_transaction_hash)
print(simple_storage.functions.retrieve().call())  # 27
