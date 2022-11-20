from brownie import network, AdvancedCollectible
from helpful_scripts import get_breed, get_account, OPENSEA_URL

dog_metadata_dic = {
    "PUG": "https://ipfs.io/ipfs/Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json",
    "SHIBA_INU": "https://ipfs.io/ipfs/QmdryoExpgEQQQgJPoruwGJyZmz6SqV4FRTX1i73CT3iXn?filename=1-SHIBA_INU.json",
    "ST_BERNARD": "https://ipfs.io/ipfs/QmbBnUjyHHN7Ytq9xDsYF9sucZdDJLRkWz7vnZfrjMXMxs?filename=2-ST_BERNARD.json",
}


def main():
    print(f"Working on {network.show_active()}")
    advancedcollectible = AdvancedCollectible[-1]
    no_of_collectibles = advancedcollectible.tokencounter()
    print(f"You have {no_of_collectibles} collectibles!")
    for token_id in range(no_of_collectibles):
        breed = get_breed(advancedcollectible.tokenIdtoBreed(token_id))
        if not advancedcollectible.tokenUri(token_id).startswith("https://"):
            print(f"Setting Token URI of {token_id}")
            settoken_URI(token_id, advancedcollectible)


def settoken_URI(token_id, nft_contract, token_URI):
    account = get_account()
    tx = AdvancedCollectible.setTokenURI(token_id, token_URI, {"from": account})
    tx.wait(1)
    print(
        f"You can view your nft at {OPENSEA_URL.format(nft_contract.address, token_id)}"
    )
    print("Wait upto 20 minutes and hit refresh")
