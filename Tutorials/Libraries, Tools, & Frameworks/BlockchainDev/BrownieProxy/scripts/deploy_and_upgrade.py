from scripts.utils import get_account, encode_function_data, upgrade
from brownie import (
    network,
    Box,
    BoxV2,
    Contract,
    ProxyAdmin,
    TransparentUpgradeableProxy,
)


def deploy_and_upgrade():
    account = get_account()
    print(f"Deploying to {network.show_active()}")
    # Box is the implementation contract.
    box = Box.deploy({"from": account})
    # Deploy the Proxy contract.
    proxy_admin = ProxyAdmin.deploy({"from": account})

    # initializer = (box.store, 1)
    box_encoded_initializer_function = encode_function_data()
    proxy = TransparentUpgradeableProxy.deploy(
        box.address,
        proxy_admin.address,
        box_encoded_initializer_function,
        {"from": account, "gas_limit": 1_000_000},
    )
    print(f"Proxy deployed to {proxy}, you can now upgrade to v2!")
    # We want to call from the proxy, NOT the box contract.
    # box.store(1)

    # This assigns the Box ABI to the proxy address.
    # Normally this would error out, but it works since the proxy will delegate all of its calls to the Box contract.
    proxy_box = Contract.from_abi("Box", proxy.address, Box.abi)
    proxy_box.store(1, {"from": account}).wait(1)
    print(proxy_box.retrieve())

    # Upgrade to BoxV2!
    box_v2 = BoxV2.deploy({"from": account})
    upgrade_transaction = upgrade(
        account, proxy, box_v2.address, proxy_admin_contract=proxy_admin
    )
    print("Proxy has been upgraded!")
    proxy_box = Contract.from_abi("BoxV2", proxy.address, BoxV2.abi)
    proxy_box.increment({"from": account}).wait(1)
    print(proxy_box.retrieve())


def main():
    deploy_and_upgrade()
