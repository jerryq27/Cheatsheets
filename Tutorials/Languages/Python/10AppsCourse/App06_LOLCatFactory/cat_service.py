import os
import shutil

import requests


def get_cat(folder, name):
    url = "http://consuming-python-services-api.azurewebsites.net/cats/random"
    data = get_url_data(url)
    save_image(folder, name, data)


def get_url_data(url):
    # Since we are getting raw data, setting stream to true will ensure it is downloaded correctly.
    # Also, streaming will avoid loading the whole file into memory, and download it in chunks.
    response = requests.get(url, stream=True)
    return response.raw


def save_image(folder, name, data):
    file_name = os.path.join(folder, name + ".jpg")
    with open(file_name, "wb") as output_file:  # 'wb' to write bytes, since we're dealing with raw low-level data.
        shutil.copyfileobj(data, output_file)
    print("done.")
