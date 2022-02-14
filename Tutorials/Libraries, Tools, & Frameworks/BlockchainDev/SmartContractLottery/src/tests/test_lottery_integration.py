from brownie import network
import pytest
from scripts.deploy_lottery import deploy_lottery
from scripts.utils import get_account, fund_with_link, LOCAL_BLOCKCHAIN_ENVIRONMENTS
import time


def test_can_pick_winner():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()
    lottery = deploy_lottery()
    account = get_account()
    lottery.startLottery({"from": account})
    lottery.enter({"from": account, "value": lottery.getEntranceFee()})
    lottery.enter({"from": account, "value": lottery.getEntranceFee()})

    fund_with_link(lottery)
    time.sleep(60)
    lottery.endLottery({"from": account})
    assert lottery.recentWinner() == account
    assert lottery.balance() == 0
