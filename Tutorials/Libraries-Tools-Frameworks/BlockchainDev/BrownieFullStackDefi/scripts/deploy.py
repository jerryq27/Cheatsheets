import os
import shutil
import yaml
import json
from scripts.utils import get_account, get_contract
from brownie import DappToken, TokenFarm, network, config
from web3 import Web3

KEPT_BALANCE = Web3.toWei(100, "ether")


def deploy_token_farm_and_dapp_token(do_frontend_update=False):
    account = get_account()
    dapp_token = DappToken.deploy({"from": account})
    token_farm = TokenFarm.deploy(
        dapp_token.address,
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"],
    )
    transaction = dapp_token.transfer(
        token_farm.address, dapp_token.totalSupply() - KEPT_BALANCE, {"from": account}
    ).wait(1)

    # DAPP token, WETH token, FAU token
    weth_token = get_contract("weth_token")
    fau_token = get_contract("fau_token")
    dict_of_allowed_tokens = {
        dapp_token: get_contract("dai_usd_price_feed"),
        fau_token: get_contract("dai_usd_price_feed"),
        weth_token: get_contract("eth_usd_price_feed"),
    }

    add_allowed_tokens(token_farm, dict_of_allowed_tokens, account)
    # Update the frontend.
    if do_frontend_update:
        update_frontend()
    # For the tests.
    return token_farm, dapp_token


def add_allowed_tokens(token_farm, dict_of_allowed_tokens, account):
    for token in dict_of_allowed_tokens:
        add_transaction = token_farm.addAllowedTokens(token.address, {"from": account})
        add_transaction.wait(1)

        set_transaction = token_farm.setPriceFeedContract(
            token.address, dict_of_allowed_tokens[token], {"from": account}
        )
        set_transaction.wait(1)
    return token_farm


def update_frontend():
    """
    This function sends brownie-config.yamnl and the build
    folder to the frontend."""

    # Send build/
    copy_folders_to_frontend("./build", "./frontend/src/chain-info")

    # Send brownie_config.yaml
    with open("brownie-config.yaml", "r") as brownie_config:
        # yaml.load() loads the yaml file into a dictionary.
        config_dict = yaml.load(brownie_config, Loader=yaml.FullLoader)
        with open("./frontend/src/brownie-config.json", "w") as brownie_config_json:
            json.dump(config_dict, brownie_config_json)
    print("Frontend upated!")


def copy_folders_to_frontend(src, destination):
    if os.path.exists(destination):
        shutil.rmtree(destination)
    shutil.copytree(src, destination)


def main():
    deploy_token_farm_and_dapp_token(do_frontend_update=True)
