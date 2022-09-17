from brownie import accounts, network, config, VRFCoordinatorMock, LinkToken, Contract

LOCAL_DEVELOPMENT_ENVIRONMENTS = [
    "hardhat, ganache, mainnet-fork, mainnet-fork-dev, ganache-cli, development"
]
OPENSEA_URL = "https://testnets.opensea.io/assets/{}/{}"

contract_to_mock = {"vrf_coordinator": VRFCoordinatorMock, "link_token": LinkToken}


def get_contract(contract_name):
    """
    This function will either:
        - Get an address from the config
        - Or deploy a mock to use for a network that doesn't have the contract

    Args:
        contract_name (string): This is the name of the contract that we will get
        from the config or deploy

    Returns:
        brownie.network.contract.ProjectContract: This is the most recently deployed
        Contract of the type specified by the dictionary. This could either be a mock
        or a 'real' contract from live network.
    """
    contract_type = contract_to_mock[contract_name]
    if network.show_active() in LOCAL_DEVELOPMENT_ENVIRONMENTS:
        if len(contract_type) <= 0:
            deploy_mocks()
        contract = contract_type[-1]
    else:
        contract_address = config["networks"][network.show_active()][contract_name]
        contract = Contract.from_abi(
            contract_type._name, contract_address, contract_type.abi
        )
    return contract


def deploy_mocks():
    """
    Use this script if you want to deploy mocks to a testnet
    """
    print(f"The active network is {network.show_active()}")
    print("Deploying mocks...")
    account = get_account()
    print("Deploying mock LinkToken...")
    link_token = LinkToken.deploy({"from": account})
    print(f"LinkToken deployed to {link_token.address}")
    print("Deploying Mock VRFCoordinator...")
    vrf_coordinator = VRFCoordinatorMock.deploy(link_token, {"from": account})
    print(f"VRFCoordinator deployed to {vrf_coordinator.address}")
    print("All done!")


def get_account(id=None, index=None):
    if index:
        return accounts[index]
    if network.show_active() in LOCAL_DEVELOPMENT_ENVIRONMENTS:
        return accounts[0]
    if id:
        return accounts.load(id)
    return accounts.add(config["wallets"]["from_key"])
