from brownie import AdvancedCollectible, network, config
from scripts.advanced_collectible.deploy_and_create import deploy_create
from scripts.helpful_scripts import (
    get_account,
    OPENSEA_URL,
    get_contract,
    fundedwithlink,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)
import pytest


def test_create_advaanced_collectible():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()

    advanced_collectible, creation_tx = deploy_create()
    requestId = creation_tx.events["RequestedCollectible"]["requestId"]
    random_number = 777
    get_contract("vrf_coordinator").callBackWithRandomness(
        requestId, random_number, advanced_collectible.address, {"from": get_account()}
    )

    assert advanced_collectible.tokenCounter() == 1
    assert advanced_collectible.tokenIdToBreed(0) == random_number % 3
