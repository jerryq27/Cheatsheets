from brownie import SimpleStorage, accounts, config, network


def test_deploy():
    # Arrange
    # Act
    # Assert

    # Arrange
    account = accounts[0]
    # Act
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrieve()
    expected = 0
    # Assert
    assert starting_value == expected


def test_updating_simple_storage():
    # Arrange
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    # Act
    expected = 27
    simple_storage.store(expected, {"from": account})
    # Assert
    assert expected == simple_storage.retrieve()


def get_account():
    return (
        accounts[0]
        if network.show_active() == "development"
        else accounts.add(config["wallets"]["from_key"])
    )
