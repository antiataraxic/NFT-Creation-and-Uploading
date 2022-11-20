from webbrowser import get
from scripts.helpful_scripts import LOCAL_BLOCKCHAIN_ENVIRONMENTS, get_account
from brownie import SimpleCollectible, network
from scripts.deploy_and_create import deploy_create
import pytest


def test_can_create_simple_collectible():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for local testing!")

    account = get_account()
    simple_collectible = deploy_create()
    assert simple_collectible.ownerOf(0) == account
