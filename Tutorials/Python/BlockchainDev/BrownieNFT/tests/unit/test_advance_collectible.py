from random import random
import pytest
from brownie import network
from scripts.utils import get_account, get_contract, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from scripts.advance_collectible.deploy_create import deploy


def test_can_create_advance_collectible():
    # Deploy contract
    # Create an NFT
    # Get random breed back
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Skipping only for local testing.")
    # Act
    advance_collectible, create_transactioin = deploy()
    requestId = create_transactioin.events["RequestedCollectible"]["requestId"]

    random_num = 777
    get_contract("vrf_coordinator").callBackWithRandomness(
        requestId, random_num, advance_collectible.address, {"from": get_account()}
    )
    # Assert
    assert advance_collectible.tokenCounter() == 1
    assert advance_collectible.tokenIdToBreed(0) == random_num % 3
