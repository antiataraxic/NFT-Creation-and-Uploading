from brownie import SimpleCollectible
from scripts.helpful_scripts import get_account, OPENSEA_URL

sample_token_URI = "https://ipfs.io/ipfs/Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json"


def deploy_create_simple():
    account = get_account()
    simplecollectible = SimpleCollectible.deploy({"from": account})
    tx = simplecollectible.createCollectible(sample_token_URI, {"from": account})
    tx.wait(1)
    print(
        f"Simple Collectible created at {OPENSEA_URL.format(simplecollectible.address, simplecollectible.tokencounter() - 1)}"
    )
    return simplecollectible


def main():
    deploy_create()
