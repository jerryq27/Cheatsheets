import pytest
import time
from brownie import network
from scripts.utils import get_account, get_contract, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from scripts.advance_collectible.deploy_create import deploy


def test_can_create_advance_collectible_integration():
    # Deploy contract
    # Create an NFT
    # Get random breed back
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Skipping only for integration testing.")
    # Act
    advance_collectible, create_transactioin = deploy()
    time.sleep(60)

    # Assert
    assert advance_collectible.tokenCounter() == 1
