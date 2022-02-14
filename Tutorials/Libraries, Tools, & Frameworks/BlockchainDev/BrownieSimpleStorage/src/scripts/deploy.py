import os
from brownie import accounts, config, SimpleStorage


def deploy_simple_storage():
    # account = accounts.add(os.getenv("PRIVATE_KEY"))
    # account = accounts.add(config["wallets"]["from_key"])

    account = accounts[0]
    # print(account)
    simple_storage = SimpleStorage.deploy({"from": account})
    # print(simple_storage)
    stored_value = simple_storage.retrieve()
    print(stored_value)
    transaction = simple_storage.store(27, {"from": account})
    transaction.wait(1)  # Wait for 1 block AKA wait for the transaction to finish.
    updated_stored_value = simple_storage.retrieve()
    print(updated_stored_value)


def main():
    deploy_simple_storage()
