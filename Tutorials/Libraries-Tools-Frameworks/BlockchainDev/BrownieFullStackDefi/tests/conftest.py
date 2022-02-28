import pytest
from web3 import Web3

# Essentially a static variable.
@pytest.fixture
def amount_staked():
    return Web3.toWei(1, "ether")
