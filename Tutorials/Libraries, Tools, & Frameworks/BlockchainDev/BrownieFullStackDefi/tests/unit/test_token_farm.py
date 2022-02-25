from brownie import network, exceptions
from scripts.deploy import deploy_token_farm_and_dapp_token
from scripts.utils import (
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
    INITIAL_VALUE,
    get_account,
    get_contract,
)
import pytest


"""
Unit Tests for the TokenFarm.sol Contract functions.
"""


def test_set_price_feed_contract():
    # Arrange
    net = network.show_active()
    if net not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for local testing!")

    account = get_account()
    non_owner_account = get_account(index=1)
    token_farm, dapp_token = deploy_token_farm_and_dapp_token()

    # Act
    price_feed_address = get_contract("eth_usd_price_feed")
    token_farm.setPriceFeedContract(
        dapp_token.address, price_feed_address, {"from": account}
    ).wait(1)

    # Assert
    # Note: Brownie automatically knows that if a Contract object is being passed into an address type
    # parameter in Solidity, to use the address of the Contract object.

    # Test the price feed has been updated
    assert token_farm.tokenPriceFeedMapping(dapp_token.address) == price_feed_address

    # Test that a different account besides the owner can't call this.
    with pytest.raises(exceptions.VirtualMachineError):
        # If this raises the 'with error', the test should should pass. otherwise it fails.
        token_farm.setPriceFeedContract(
            dapp_token.address, price_feed_address, {"from": non_owner_account}
        ).wait(1)


# pytest automatically grabs the 'amount_staked' fixture from conftest.py.
def test_stake_tokens(amount_staked):
    # Arrange
    net = network.show_active()
    if net not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for local testing!")

    account = get_account()
    token_farm, dapp_token = deploy_token_farm_and_dapp_token()

    # Act
    dapp_token.approve(token_farm.address, amount_staked, {"from": account}).wait(1)
    token_farm.stakeTokens(amount_staked, dapp_token.address, {"from": account}).wait(1)

    # Assert

    # The balance for this account should be the same ammount that was sent.
    assert (
        # stakingBalance is a mapping of a mapping, so it needs two keys. It's handled by Brownie by passing in two arguments.
        token_farm.stakingBalance(dapp_token.address, account.address)
        == amount_staked
    )
    # New account should only have one unique token (DAPP).
    assert token_farm.uniqueTokensStaked(account.address) == 1
    # Stakers list should only have one stake, the account staking.
    assert token_farm.stakers(0) == account.address
    # For other tests that need a token farm with some staked tokens.
    return token_farm, dapp_token


def test_issue_tokens(amount_staked):
    # Arrange
    net = network.show_active()
    if net not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for local testing!")

    account = get_account()
    token_farm, dapp_token = test_stake_tokens(amount_staked)
    starting_balance = dapp_token.balanceOf(account.address)

    # Act
    token_farm.issueTokens({"from": account}).wait(1)

    # Assert

    # Rewarding 2000 DAPP tokens for every 1 ETH, since ETH is at $2000.
    assert dapp_token.balanceOf(account.address) == starting_balance + INITIAL_VALUE


def test_token_is_allowed():
    # Arrange
    WBTC = "0xe0f131fb595000d7e54049efe5c40dca9572469c"
    net = network.show_active()
    if net not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for local testing!")

    account = get_account()
    non_owner_account = get_account(index=1)
    token_farm, dapp_token = deploy_token_farm_and_dapp_token()

    # Act
    fau_token = get_contract("fau_token")
    weth_token = get_contract("weth_token")

    # transaction = token_farm.transact.allowedTokens(fau_token).wait(1)
    # print(f"Transaction: {transaction.return_value}")

    # Assert
    # assert fau_token in token_farm.allowedTokens()
    # assert weth_token in token_farm.allowedTokens()
    # assert WBTC not in token_farm.allowedTokens()

    with pytest.raises(exceptions.VirtualMachineError):
        token_farm.addAllowedTokens(WBTC, {"from": non_owner_account})


def test_get_eth_value_of_token():
    pass
