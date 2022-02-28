from brownie import accounts, MyToken
from scripts.utils import get_account
from web3 import Web3


def deploy():
    # account = accounts[0]
    account = get_account()
    print(account.address)
    # my_token = MyToken.deploy(1000, {"from": account})
    my_token = MyToken.deploy(Web3.toWei(1000, "ether"), {"from": account})
    print(
        f"My token was deployed at {my_token.address} with the name: {my_token.name()}"
    )


def main():
    deploy()
