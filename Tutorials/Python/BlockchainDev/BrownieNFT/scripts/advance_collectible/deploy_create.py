from scripts.utils import get_account, OPENSEA_URL, get_contract
from brownie import AdvanceCollectible, network, config
from web3 import Web3

sample_token_uri = "https://ipfs.io/ipfs/Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json"


def deploy():
    net = network.show_active()
    account = get_account()
    # Currently OpenSea testnet only works on the Rinkeby, so we'll have to stick with Rinkeby.
    advance_collectible = AdvanceCollectible.deploy(
        get_contract("vrf_coordinator"),
        get_contract("link_token"),
        config["networks"][net]["keyhash"],
        config["networks"][net]["fee"],
        {"from": account},
        publish_source=True,
    )
    fund_with_link(advance_collectible.address)
    create_transaction = advance_collectible.createCollectible({"from": account})
    create_transaction.wait(1)
    print("New token has been created!")
    return (
        advance_collectible,
        create_transaction,
    )  # Need the requestId from create_transaction too!


def fund_with_link(
    contract_address, account=None, link_token=None, amount=Web3.toWei(1, "ether")
):
    account = account if account else get_account()
    link_token = link_token if link_token else get_contract("link_token")
    fund_transaction = link_token.transfer(contract_address, amount, {"from": account})
    fund_transaction.wait(1)
    print(f"Funded {contract_address} with {amount} LINK!")


def main():
    deploy()
