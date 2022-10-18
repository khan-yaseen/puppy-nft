from brownie import network, AdvancedCollectible
from scripts.helpful_scripts import OPENSEA_URL, get_breed, get_account

dog_metadata_dic = {
    0: "https://ipfs.io/ipfs/QmTWxcKAvRp7rX9HbY6qq4KMUeGrvxUcMxxs9FotddNxus?filename=0-ST_BERNARD.json",
    1: "https://ipfs.io/ipfs/QmTWxcKAvRp7rX9HbY6qq4KMUeGrvxUcMxxs9FotddNxus?filename=1-ST_BERNARD.json",
    2: "https://ipfs.io/ipfs/QmXo1YBeXEy6VzGWyD2RGD5dxJvGZ3bm3jLitTBr2j8wXU?filename=2-SHIBA_INU.json",
    3: "https://ipfs.io/ipfs/QmXo1YBeXEy6VzGWyD2RGD5dxJvGZ3bm3jLitTBr2j8wXU?filename=3-SHIBA_INU.json",
    4: "https://ipfs.io/ipfs/QmTWxcKAvRp7rX9HbY6qq4KMUeGrvxUcMxxs9FotddNxus?filename=4-ST_BERNARD.json",
    5: "https://ipfs.io/ipfs/QmaXd99UnLtwtgusJPLavZHTf6LucD1PPvGeAd1UtnM2sR?filename=5-PUG.json",
}

# dog_metadata_dic = {
#     "PUG": "https://ipfs.io/ipfs/Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json",
#     "SHIBA_INU": "https://ipfs.io/ipfs/QmdryoExpgEQQQgJPoruwGJyZmz6SqV4FRTX1i73CT3iXn?filename=1-SHIBA_INU.json",
#     "ST_BERNARD": "https://ipfs.io/ipfs/QmbBnUjyHHN7Ytq9xDsYF9sucZdDJLRkWz7vnZfrjMXMxs?filename=2-ST_BERNARD.json",
# }


def main():
    print(f"Working on {network.show_active()}")
    advanced_collectible = AdvancedCollectible[-2]
    number_of_collectibles = advanced_collectible.tokenCounter()
    print(f"You have {number_of_collectibles} tokenIds")
    for token_id in range(number_of_collectibles):
        breed = get_breed(advanced_collectible.tokenIdToBreed(token_id))
        if not advanced_collectible.tokenURI(token_id).startswith("https://"):
            print(f"Setting tokenURI of {token_id}")
            set_tokenURI(token_id, advanced_collectible, dog_metadata_dic[token_id])


def set_tokenURI(token_id, nft_contract, tokenURI):
    account = get_account()
    tx = nft_contract.setTokenURI(token_id, tokenURI, {"from": account})
    tx.wait(1)
    print(
        f"Awesome! You can view your NFT at  {OPENSEA_URL.format(nft_contract.address, token_id)}"
    )
    print("Please wati up to 20 minutes, and hit the refresh metadata button")
