from brownie import network, config, accounts, MockV3Aggregator

FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]

DECIMALS = 8
STARTING_PRICE = 200_000_000_000

# Util function to return an account provided by Brownie for testing or the one defined in brownie-config.yaml
def get_account():
    # if network.show_active() == "development":
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    # mock deploy
    print(f"The active network is {network.show_active()}")

    if len(MockV3Aggregator) <= 0:
        print("Deploying Mocks...")
        # mock_aggregator = MockV3Aggregator.deploy(
        #     18, 2_000_000_000_000_000_000, {"from": account}
        # )
        MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": get_account()})
    print("Mocks deployed!")
