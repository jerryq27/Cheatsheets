from scripts.utils import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from scripts.simple_collectible.deploy_create import deploy
from brownie import network
import pytest

net = network.show_active()


def test_can_create_simple_collectible():
    if net in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()

    simple_collectible = deploy()
    assert simple_collectible.ownerOf(0) == get_account()
