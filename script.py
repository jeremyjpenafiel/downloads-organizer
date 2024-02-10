import os
from pathlib import Path


DOWNLOADS = Path.home() / 'Downloads'
FOLDER_NAMES = ["PDFs", "Images", "Videos", "Word Documents"]
FOLDER_DICT = {
    ".pdf": "PDFs",
    ".jpg": "JPG",
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


# TODO: Check if directory of current script is Downloads
# if os.curdir != DOWNLOADS:
#     raise Exception("Move this file to your Downloads folder")

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
            os.rename(file.path, file.path + FOLDER_DICT[file_type])

# TODO: Schedule every day?



