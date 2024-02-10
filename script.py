"""Downloads organizer program for my gf Kae <3"""

import os
from pathlib import Path
import logging
import sys

DOWNLOADS = str(Path.home() / 'Downloads')
FOLDER_DICT = {
    ".pdf": "PDFs",
    ".jpg": "Images",
    ".png": "Images",
    ".jpeg": "Images",
    ".gif": "Images",
    ".bmp": "Images",
    ".tiff": "Images",
    "mp4": "Videos",
    ".mov": "Videos",
    ".mpg": "Videos",
    ".avi": "Videos",
    "doc": "Word Documents",
    ".docx": "Word Documents"}


def exit_function() -> None:
    """Exits the program"""
    exit_input = input("Press enter to exit...")

    while exit_input:
        exit_input = input("Press enter to exit...")

    print("Exiting...")
    sys.exit(0)


# TODO: Check if directory of current script is Downloads
if os.getcwd() != DOWNLOADS:
    print(f"Current directory is {os.getcwd()}")
    e = "Hi babi q, you need to move this file to your Downloads folder and then you can run it"
    logging.error(e)
    exit_function()

# TODO: Check if folders to be made already exists

for folder in FOLDER_DICT.values():
    path: str = f"{os.curdir}/{folder}"
    if not os.path.exists(path):
        os.mkdir(path)

# TODO: Move all files to corresponding folders
for file in os.scandir():
    if not file.is_file():
        continue
        
    for file_type in FOLDER_DICT.keys():
        if file.name.endswith(file_type):
            new_path = f"{os.curdir}/{FOLDER_DICT[file_type]}/{file.name}"
            os.rename(file.path, new_path)

# TODO: Schedule every day?
print("Done organizing your files! Enjoy your organized folder, babi. I love you <3")
exit_function()