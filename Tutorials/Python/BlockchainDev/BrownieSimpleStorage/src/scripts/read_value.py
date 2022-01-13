from brownie import SimpleStorage, accounts, config


def read_contract():
    simple_storage = SimpleStorage[-1]  # Returns the most recent deployment
    # Need ABI and address of the contract, which Brownie already knows!
    # So we can just do this:
    print(simple_storage.retrieve())


def main():
    read_contract()
