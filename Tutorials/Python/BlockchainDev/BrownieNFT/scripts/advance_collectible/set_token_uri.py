from brownie import network, AdvanceCollectible
from scripts.utils import get_breed, get_account, OPENSEA_URL

breed_to_metadata = {
    "PUG": "https://ipfs.io/ipfs/QmZKUjW9j5tBG336Y4NLxnGuw3J96VqU76C2DHF9KPS4c2?filename=0-PUG.json",
    "SHIBA_INU": "https://ipfs.io/ipfs/QmcThh7p4MA2rQpvjbxApBbyNL7nUScu7ZprEE2iiX9t1j?filename=1-SHIBA_INU.json",
    "ST_BERNARD": "",
}


def main():
    print(f"Working on {network.show_active()}")
    advance_collectible = AdvanceCollectible[-1]
    num_of_collectibles = advance_collectible.tokenCounter()
    print(f"You have {num_of_collectibles} tokenIds")

    for token_id in range(num_of_collectibles):
        breed = get_breed(advance_collectible.tokenIdToBreed(token_id))

        if not advance_collectible.tokenURI(token_id).startswith("https://"):
            print(f"Setting tokenURI of {token_id}")
            set_tokenURI(token_id, advance_collectible, breed_to_metadata[breed])


def set_tokenURI(token_id, nft_contract, tokenURI):
    account = get_account()
    transaction = nft_contract.setTokenURI(token_id, tokenURI, {"from": account})
    transaction.wait(1)

    print(
        f"You can view your NFT at {OPENSEA_URL.format(nft_contract.address, token_id)}"
    )
