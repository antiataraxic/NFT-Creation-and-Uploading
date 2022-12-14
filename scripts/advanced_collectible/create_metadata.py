from importlib.metadata import metadata
from brownie import AdvancedCollectible, network
from scripts.helpful_scripts import get_breed
from metadata.sample_uri import metadata_template
from pathlib import Path
import requests
import json
import os

breed_to_image_uri = {
    "PUG": "https://ipfs.io/ipfs/QmSsYRx3LpDAb1GZQm7zZ1AuHZjfbPkD6J7s9r41xu1mf8?filename=pug.png",
    "SHIBA_INU": "https://ipfs.io/ipfs/QmYx6GsYAKnNzZ9A6NvEKV9nf1VaDzJrqDR23Y8YSkebLU?filename=shiba-inu.png",
    "ST_BERNARD": "https://ipfs.io/ipfs/QmUPjADFGEKmfohdTaNcWhp7VGk26h5jXDA7v3VtTnTLcW?filename=st-bernard.png",
}


def main():
    advcollectible = AdvancedCollectible[-1]
    no_of_adv_collectibles = advcollectible.tokencounter()
    print(f"You have created {no_of_adv_collectibles} collectibles!")
    for token_id in range(no_of_adv_collectibles):
        breed = get_breed(advcollectible.breedAssigned(token_id))
        metadata_file_name = (
            f"./metadata/{network.show_active()}/{token_id}-{breed}.json"
        )
        collectible_metadata = metadata_template
        if Path(metadata_file_name).exists():
            print(f"{metadata_file_name} already exists, Delete it to overwrite.")
        else:
            print(f"Creating metadata file {metadata_file_name}")
        collectible_metadata["name"] = breed
        collectible_metadata["description"] = "An adorable {breed} dog."
        image_path = "./img/" + breed.lower().replace("_", "-") + ".png"
        image_uri = None
        if os.getenv("UPLOAD_IPFS") == "true":
            image_uri = upload_to_ipfs(image_path)

        image_uri = image_uri if image_uri else breed_to_image_uri[breed]
        collectible_metadata["image_uri"] = image_uri
        with open(metadata_file_name, "w") as file:
            json.dump(collectible_metadata, file)
            if os.getenv("UPLOAD_IPFS") == "true":
                upload_to_ipfs(metadata_file_name)


def upload_to_ipfs(filepath):
    with Path(filepath).open("rb") as fp:
        image_binary = fp.read()
        ipfs_url = "http://127.0.0.1:5001"
        endpoint = "/api/v0/add"
        response = requests.post(ipfs_url + endpoint, files={"file": image_binary})
        ipfs_hash = response.json()["Hash"]
        filename = filepath.split("/")[-1:][0]
        image_uri = f"https://ipfs.io/ipfs/{ipfs_hash}?filename={filename}"
        print(image_uri)
        return image_uri
