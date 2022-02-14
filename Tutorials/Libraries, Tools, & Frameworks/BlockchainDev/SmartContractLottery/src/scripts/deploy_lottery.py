from scripts.utils import get_account, get_contract, fund_with_link
from brownie import Lottery, config, network
import time


def deploy_lottery():
    account = get_account()
    lottery = Lottery.deploy(
        get_contract("eth_usd_price_feed").address,
        get_contract("vrf_coordinator").address,
        get_contract("link_token").address,
        config["networks"][network.show_active()]["fee"],
        config["networks"][network.show_active()]["keyhash"],
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify", False),
    )

    print("Deployed lottery!")
    return lottery


def start_lottery():
    account = get_account()
    lottery = Lottery[-1]
    # Add this wait, otherwise things might crash since we're trying to run code afterwards and the contract might not have been deployed yet.
    lottery.startLottery({"from": account}).wait(1)

    print("Lottery started!")


def enter_lottery():
    account = get_account()
    lottery = Lottery[-1]
    value = lottery.getEntranceFee() + 100000000  # Adding a little bit of ETH.
    lottery.enter({"from": account, "value": value}).wait(1)

    print("You entered the lottery!")


def end_lottery():
    account = get_account()
    lottery = Lottery[-1]
    # Fund contract, then end the lottery
    fund_with_link(lottery.address).wait(1)
    lottery.endLottery({"from": account}).wait(1)
    time.sleep(60)

    print(f"{lottery.recentWinner()} is the winner!")


def main():
    deploy_lottery()
    start_lottery()
    enter_lottery()
    end_lottery()
