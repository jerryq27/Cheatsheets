from webbrowser import get
from scripts.get_weth import get_weth
from scripts.utils import get_account
from brownie import network, config, interface
from web3 import Web3

amount = Web3.toWei(0.1, "ether")


def main():
    net = network.show_active()
    account = get_account()
    erc20_address = config["networks"][net]["weth_token"]

    if net in ["mainnet-fork"]:
        get_weth()
    # ABI
    # Address
    lending_pool = get_lending_pool()
    # Approve sending our ERC20 tokens.
    approve_erc20(amount, lending_pool.address, erc20_address, account)
    print("Depositing...")
    transaction = lending_pool.deposit(
        erc20_address, amount, account.address, 0, {"from": account}
    )
    transaction.wait(1)
    print("Deposited!")
    borrowable_eth, total_debt = get_borrowable_data(lending_pool, account)

    # DAI in terms of ETH
    dai_eth_price = get_asset_price(
        config["networks"][network.show_active()]["dai_eth_price_feed"]
    )
    amount_dai_to_borrow = (1 / dai_eth_price) * (borrowable_eth * 0.95)
    print(f"We are going to borrow {amount_dai_to_borrow} DAI")

    dai_address = config["networks"][network.show_active()]["dai_token"]
    borrow_transaction = lending_pool.borrow(
        dai_address,
        Web3.toWei(amount_dai_to_borrow, "ether"),
        1,
        0,
        account.address,
        {"from": account},
    )
    borrow_transaction.wait(1)
    print("Borrowed some DAI!")
    get_borrowable_data(lending_pool, account)

    # Repay
    # repay_all(amount, lending_pool, account)
    print(
        "Finished depositing, borrowing, and repaying with Brownie, Aave, and Chainlink!"
    )


def repay_all(amount, lending_pool, account):
    approve_erc20(
        Web3.toWei(amount, "ether"),
        lending_pool,
        config["networks"][network.show_active()]["dai_token"],
        account,
    )
    repay_transaction = lending_pool.repay(
        config["networks"][network.show_active()]["dai_token"],
        amount,
        1,
        account.address,
        {"from": account},
    )
    repay_transaction.wait(1)
    print("Repaid!")


def get_asset_price(price_feed_address):
    # ABI - Can get by working directly with interface?
    # ADdress
    dai_eth_price_feed = interface.IAggregatorV3(price_feed_address)
    latest_price = dai_eth_price_feed.latestRoundData()[1]
    converted_latest_price = Web3.fromWei(latest_price, "ether")
    print(f"The DAI/ETH price is {converted_latest_price}")
    return float(converted_latest_price)


def get_borrowable_data(lending_pool, account):
    (
        total_collateral_eth,
        total_debt_eth,
        available_borrow_eth,
        current_liquidation_threshold,
        ltc,
        health_factor,
    ) = lending_pool.getUserAccountData(account.address)

    available_borrow_eth = Web3.fromWei(available_borrow_eth, "ether")
    total_collateral_eth = Web3.fromWei(total_collateral_eth, "ether")
    total_debt_eth = Web3.fromWei(total_debt_eth, "ether")

    print(f"You have {total_collateral_eth} worth of ETH deposited.")
    print(f"You have {total_debt_eth} worth of ETH borrowed.")
    print(f"You can borrow {available_borrow_eth} worth of ETH.")
    return (float(available_borrow_eth), float(total_debt_eth))


def approve_erc20(amount, spender, erc20_address, account):
    # ABI
    # Address
    print("Approving ERC20 token...")
    erc20 = interface.IERC20(erc20_address)
    transaction = erc20.approve(spender, amount, {"from": account})
    transaction.wait(1)
    print("Approved!")
    return transaction


def get_lending_pool():
    # Address
    lending_pool_addresses_provider = interface.ILendingPoolAddressesProvider(
        config["networks"][network.show_active()]["lending_pool_addresses_provider"]
    )
    lending_pool_address = lending_pool_addresses_provider.getLendingPool()

    # ABI
    lending_pool = interface.ILendingPool(lending_pool_address)
    return lending_pool
