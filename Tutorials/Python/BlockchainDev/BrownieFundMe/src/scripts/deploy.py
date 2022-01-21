from brownie import FundMe, MockV3Aggregator, network, config
from scripts.utils import get_account, deploy_mocks, LOCAL_BLOCKCHAIN_ENVIRONMENTS


def deploy_fund_me():
    account = get_account()
    net = network.show_active()

    # If using Rinkeby net, use the Chainlink Rinkeby address, otherwise deploy "mocks" for local.
    if net not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][net]["eth_usd_price_feed"]
    else:
        deploy_mocks()
        # price_feed_address = mock_aggregator.address
        price_feed_address = MockV3Aggregator[-1].address

    # publish_source=True verifies the contract on Etherscan using the API key.
    fund_me = FundMe.deploy(
        # AggregatorV3Interface Rinkeby Address passed into the FundMe.sol constructor.
        price_feed_address,
        {"from": account},
        # publish_source=True,
        # using .get($KEY) in case we forget to define it in a network definition.
        publish_source=config["networks"][net].get("verify_contract"),
    )
    print(f"Contract deployed to {fund_me.address}")
    return fund_me


def main():
    deploy_fund_me()
