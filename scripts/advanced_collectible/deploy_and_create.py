from scripts.helpful_scripts import get_account, OPENSEA_URL, get_contract
from brownie import AdvancedCollectible, config, network


def deploy_and_create():
    account = get_account()
    # We want to be able to use the deployed contracts if we are on a testnet
    # Otherwise, we want to deploy some mocks and use those
    # Goerli
    advanced_collectible = AdvancedCollectible.deploy(
        get_contract("vrf_coordinator"),
        get_contract("link_token"),
        config["networks"][network.show_active()]["key_hash"],
        config["networks"][network.show_active()]["fee"],
        {"from": account},
    )

    return advanced_collectible


def main():
    deploy_and_create()