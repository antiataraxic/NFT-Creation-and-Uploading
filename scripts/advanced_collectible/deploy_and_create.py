from brownie import AdvancedCollectible, network, config
from scripts.helpful_scripts import (
    get_account,
    OPENSEA_URL,
    get_contract,
    fundedwithlink,
)


def deploy_create():
    account = get_account()
    advancedcollectible = AdvancedCollectible.deploy(
        get_contract("vrf_coordinator").address,
        get_contract("link_token").address,
        config["networks"][network.show_active()]["keyhash"],
        config["networks"][network.show_active()]["fee"],
        {"from": account},
    )
    fundedwithlink(advancedcollectible.address)
    tx = advancedcollectible.createCollectible({"from": account})
    tx.wait(1)
    print("Creating new token!")
    return advancedcollectible, tx


def main():
    deploy_create()
