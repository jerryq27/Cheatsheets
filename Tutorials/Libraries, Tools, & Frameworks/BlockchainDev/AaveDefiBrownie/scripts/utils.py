from brownie import (
    accounts,
    network,
    config,
)

LOCAL_BLOCKCHAIN_ENVIRONMENTS = [
    "development",
    "ganache",
    "hardhat",
    "local-ganache",
    "mainnet-fork",
]

# Util function to return an account provided by Brownie for testing or the one defined in brownie-config.yaml
def get_account(index=None, id=None):
    net = network.show_active()
    if index:
        return accounts[index]
    if net in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts[0]
    if id:
        return accounts.load(id)
    # if net in config["networks"]:
    return accounts.add(config["wallets"]["from_key"])

    # return None
