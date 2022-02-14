from brownie import AdvanceCollectible, network
from scripts.utils import get_breed
from metadata.sample_metadata import metadata_template
from pathlib import Path
import requests
import json
import os

breed_to_image_uri = {
    # {'IpfsHash': 'QmSsYRx3LpDAb1GZQm7zZ1AuHZjfbPkD6J7s9r41xu1mf8', 'PinSize': 5699, 'Timestamp': '2022-02-07T04:58:41.001Z'}
    "PUG": "https://ipfs.io/ipfs/QmSsYRx3LpDAb1GZQm7zZ1AuHZjfbPkD6J7s9r41xu1mf8?filename=pug.png",
    "SHIBA_INU": "https://ipfs.io/ipfs/QmYx6GsYAKnNzZ9A6NvEKV9nf1VaDzJrqDR23Y8YSkebLU?filename=shiba-inu.png",
    "ST_BERNARD": "",
}


def main():
    advance_collectible = AdvanceCollectible[-1]
    # Loop through tokens.
    num_of_collectibles = advance_collectible.tokenCounter()
    print(f"You have created {num_of_collectibles} collectibles.")
    for token_id in range(num_of_collectibles):
        breed = get_breed(advance_collectible.tokenIdToBreed(token_id))
        metadata_filename = (
            f"./metadata/{network.show_active()}/{token_id}-{breed}.json"
        )
        collectible_metadata = metadata_template

        if Path(metadata_filename).exists():
            print(f"{metadata_filename} already exists!")
        else:
            print(f"Creating metadatafile: {metadata_filename}")
            collectible_metadata["name"] = breed
            collectible_metadata["description"] = f"An adorable {breed} pup!"

            image_path = f"./img/{breed.lower().replace('_', '-')}.png"
            image_uri = None
            if os.getenv("UPLOAD_FILES") == "true":
                image_uri = upload_to_ipfs(image_path)
            image_uri = image_uri if image_uri else breed_to_image_uri[breed]
            collectible_metadata["image"] = image_uri

            with open(metadata_filename, "w") as mdfile:
                json.dump(collectible_metadata, mdfile)

            if os.getenv("UPLOAD_FILES") == "true":
                upload_to_ipfs(metadata_filename)
                # upload_to_pinata(metadata_filename)


def upload_to_ipfs(filepath):
    with Path(filepath).open("rb") as fp:
        image_binary = fp.read()
        # Upload to IPFS

        # Install IPFS CLI
        # ipfs init
        # ipfs daemon
        # To get this WebUI url.
        ipfs_url = " http://127.0.0.1:5001"

        # Make post request to an endpoint: https://docs.ipfs.io/reference/http/api/#api-v0-add
        endpoint = "/api/v0/add"
        response = requests.post(ipfs_url + endpoint, files={"file": image_binary})
        """
        response body:
        {
            "Bytes": "<int64>",
            "Hash": "<string>", # Unique hash that represents the file.
            "Name": "<string>",
            "Size": "<string>"
        }
        """
        ipfs_hash = response.json()["Hash"]
        filename = filepath.split("/")[-1:][0]
        image_uri = f"https://ipfs.io/ipfs/{ipfs_hash}?filename={filename}"
        print(image_uri)
        return image_uri


# Alternative function using Pinata.
def upload_to_pinata(filepath):
    # https://docs.pinata.cloud/api-pinning/pin-file
    pinata_url = "https://api.pinata.cloud/"
    endpoint = "pinning/pinFileToIPFS"

    filename = filepath.split("/")[-1:][0]
    headers = {
        "pinata_api_key": os.getenv("PINATA_API_KEY"),
        "pinata_secret_api_key": os.getenv("PINATA_API_SECRET"),
    }

    with Path(filepath).open("rb") as fp:
        image_binary = fp.read()
        response = requests.post(
            pinata_url + endpoint,
            files={"file": (filename, image_binary)},
            headers=headers,
        )
    print(response.json())
