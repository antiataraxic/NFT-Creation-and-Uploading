from brownie import AdvancedCollectible, network
from scripts.advanced_collectible.deploy_and_create import deploy_create
from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
import time
import pytest


def test_integration_advanced_collectible():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for testnet or forknet testing")
    advancedcollectible, tx = deploy_create()
    time.sleep(30)

    assert advancedcollectible.tokencounter() == 1
