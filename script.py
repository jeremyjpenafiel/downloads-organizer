"""Downloads organizer program for my gf Kae <3"""

import os
from pathlib import Path
import logging
import sys
from enum import Enum


class Folders(Enum):
    IMAGES = "Images"
    PDF = "PDFs"
    VIDEOS = "Videos"
    APPS = "Applications"
    PPT = "Powerpoints"
    MUSIC = "Music"
    DOCX = "Word Documents"
    EXCEL = "Excel Files"
    ZIP = "Zips and Rars"


DOWNLOADS = str(Path.home() / 'Downloads')
FOLDER_DICT = {
    ".pdf": Folders.PDF.value,
    ".jpg": Folders.IMAGES.value,
    ".png": Folders.IMAGES.value,
    ".jpeg": Folders.IMAGES.value,
    ".heic": Folders.IMAGES.value,
    ".gif": Folders.IMAGES.value,
    ".bmp": Folders.IMAGES.value,
    ".tiff": Folders.IMAGES.value,
    ".hevc": Folders.VIDEOS.value,
    ".mp4": Folders.VIDEOS.value,
    ".mov": Folders.VIDEOS.value,
    ".mpg": Folders.VIDEOS.value,
    ".avi": Folders.VIDEOS.value,
    ".wmv": Folders.VIDEOS.value,
    ".doc": Folders.DOCX.value,
    ".docx": Folders.DOCX.value,
    ".exe": Folders.APPS.value,
    ".html": Folders.PDF.value,
    ".xlsx": Folders.EXCEL.value,
    ".xls": Folders.EXCEL.value,
    ".zip": Folders.ZIP.value,
    ".rar": Folders.ZIP.value,
    ".mp3": Folders.MUSIC.value,
    ".pptx": Folders.PPT.value,
}


def start_function() -> None:
    """Starts the program"""
    start_input = input("Hi babi q! <3 Press enter to start the program...")
    while start_input:
        start_input = input("Hi babi q! <3 Press enter to start the program...")

    print("Starting the program...")


def exit_function() -> None:
    """Exits the program"""
    exit_input = input("Press enter to exit...")

    while exit_input:
        exit_input = input("Press enter to exit...")

    print("Exiting...")
    sys.exit(0)


start_function()

# TODO: Check if directory of current script is Downloads
if os.getcwd() != DOWNLOADS:
    print(f"Current directory is {os.getcwd()}")
    e = "Hi babi q, you need to move this file to your Downloads folder and then you can run it"
    logging.error(e)
    exit_function()

# TODO: Check if folders to be made already exists

for folder in set(FOLDER_DICT.values()):
    path: str = f"{os.curdir}/{folder}"
    if not os.path.exists(path):
        os.mkdir(path)

# TODO: Move all files to corresponding folders
with os.scandir(os.getcwd()) as files:
    for file in files:
        if not file.is_file():
            continue
        for file_type in FOLDER_DICT.keys():
            if file.name.endswith(file_type):
                new_path = f"{os.curdir}/{FOLDER_DICT[file_type]}/{file.name}"
                os.rename(file.path, new_path)


# TODO: Schedule every day?
print("Done organizing your files! Enjoy your organized folder, babi. I love you <3")
exit_function()
