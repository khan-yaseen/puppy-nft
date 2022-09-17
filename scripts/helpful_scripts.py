from brownie import accounts, network, config

LOCAL_DEVELOPMENT_ENVIRONMENTS = ["hardhat, ganache, mainnet-fork, mainnet-fork-dev, ganache-cli, development"]
OPENSEA_URL = "https://testnets.opensea.io/assets/{}/{}"


def get_account(id=None, index=None):
    if index:
        return accounts[index]
    if network.show_active() in LOCAL_DEVELOPMENT_ENVIRONMENTS:
        return accounts[0]
    if id:
        return accounts.load(id)
    return accounts.add(config["wallets"]["from_key"])
