import os
import platform
import subprocess

from App06_LOLCatFactory import cat_service
from Common import app


def get_output_folder():
    output_folder = "CatPictures"

    base_folder = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(base_folder, output_folder)
    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print("Creating new directory at '{}'.".format(full_path))
        os.mkdir(full_path)

    return full_path


def download_cats(folder):
    print("Connecting to server to download cats..")
    cat_count = 8
    for i in range(1, cat_count + 1):  # 1 - 8, 8 is not inclusive.
        name = "lolcat_{}".format(i)
        print("Downloading cat {}".format(i), end=" ... ")
        cat_service.get_cat(folder, name)


def display_cats(folder):
    OS = platform.system()
    if OS == "Windows":
        print("Launching output folder in Explorer.")
        subprocess.call(["explorer", folder])
    elif OS == "Linux":
        print("Launching output folder in Files.")
        subprocess.call(["xdg-open", folder])
    elif OS == "Darwin":
        print("Launching output folder in Files.")
        subprocess.call(["open", folder])
    else:
        print("we don't support your OS: {}".format(OS))


if __name__ == '__main__':
    app.print_title("Cat Factory App")
    folder = get_output_folder()
    download_cats(folder)
    display_cats(folder)
