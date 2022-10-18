import os
from pathlib import Path
import requests
import sys

PINATA_BASE_URL = "https://api.pinata.cloud/"
endpoint = "pinning/pinFileToIPFS"
# Change this filepath
filepath = "./img/pug.png"
filename = filepath.split("/")[-1:][0]

# old headers:
# "pinata_api_key" : os.getenv("PINATA_API_KEY"),
# "pinata_api_secret": os.getenv("PINATA_API_SECRET"),

headers = {"Authorization": "Bearer " + os.getenv("PINATA_JWT_TOKEN")}


def main():
    # try:
    with Path(filepath).open("rb") as fp:
        image_binary = fp.read()
        response = requests.post(
            PINATA_BASE_URL + endpoint,
            files={"file": (filename, image_binary)},
            headers=headers,
        )
        print(response.json())


# except:
#     print(sys.exc_info()[0])
