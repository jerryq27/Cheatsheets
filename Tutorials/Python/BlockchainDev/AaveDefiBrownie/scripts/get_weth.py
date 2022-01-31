from scripts.utils import get_account
from brownie import interface, config, network


def get_weth():
    """
    Mints WETH by depositing ETH.
    Needs:
        ABI
        Address
    """
    account = get_account()
    weth = interface.IWeth(config["networks"][network.show_active()]["weth_token"])
    transaction = weth.deposit({"from": account, "value": 0.1 * (10 ** 18)})
    print("Received 0.1 WETH")
    return transaction


def main():
    get_weth()
