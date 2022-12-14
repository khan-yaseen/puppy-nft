from brownie import network
import pytest
from scripts.helpful_scripts import (
    LOCAL_DEVELOPMENT_ENVIRONMENTS,
    get_account,
    get_contract,
)
from scripts.advanced_collectible.deploy_and_create import deploy_and_create
import time


def test_can_create_advanced_collectible_integration():
    # deploy the contract
    # create an NFT
    # get a random breed back
    # Arrange
    if network.show_active() in LOCAL_DEVELOPMENT_ENVIRONMENTS:
        pytest.skip("Only for integration testing")
    # Act
    advanced_collectible = deploy_and_create()
    time.sleep(60)
    # Assert
    assert advanced_collectible.tokenCounter() == 1
