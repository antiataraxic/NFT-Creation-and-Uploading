from operator import ge
from re import A
from brownie import AdvancedCollectible
from web3 import Web3
from scripts.helpful_scripts import get_account, fundedwithlink


def create_collectible():
    account = get_account()
    advancedcollectible = AdvancedCollectible[-1]
    fundedwithlink(advancedcollectible.address)
    tx = advancedcollectible.createCollectible({"from": account})
    tx.wait(1)
    print("Creating Collectible")


def main():
    create_collectible()
