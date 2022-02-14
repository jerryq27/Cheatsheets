from scripts.utils import get_account, encode_function_data
from brownie import Contract, Box, ProxyAdmin, TransparentUpgradeableProxy


def test_proxy_delegates_calls():
    account = get_account()

    # Create the stuff we need for the OpenZeppelin Proxy class.
    # The Implementation contract, The Proxy admin contract, the encoded initializer
    box = Box.deploy({"from": account})
    proxy_admin = ProxyAdmin.deploy({"from": account})
    box_encoded_initializer_function = encode_function_data()

    # Create the OpenZeppelin TransparentUpgradeableProxy
    proxy = TransparentUpgradeableProxy.deploy(
        box.address,
        proxy_admin.address,
        box_encoded_initializer_function,
        {"from": account, "gas_limit": 1000000},
    )

    # Places the Box abi on the TransparentUpgradeableProxy
    proxy_box = Contract.from_abi("Box", proxy.address, Box.abi)
    assert proxy_box.retrieve() == 0
    proxy_box.store(1, {"from": account}).wait(1)
    assert proxy_box.retrieve() == 1
