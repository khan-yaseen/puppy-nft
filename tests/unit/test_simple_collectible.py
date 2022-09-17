from scripts.helpful_scripts import LOCAL_DEVELOPMENT_ENVIRONMENTS, get_account
from scripts.simple_collectible.deploy_and_create import deploy_and_create
import pytest
from brownie import network


def test_can_create_simple_collectible():
    print(network.show_active())
    if network.show_active() not in LOCAL_DEVELOPMENT_ENVIRONMENTS:
        pytest.skip()
    simple_collectible = deploy_and_create()
    assert simple_collectible.ownerOf(0) == get_account()
