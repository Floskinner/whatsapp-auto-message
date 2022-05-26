import json
from pathlib import Path
from typing import Union

import pyqrcode
from PIL import Image
from pyzbar.pyzbar import decode


parent_folder = Path(__file__).parent.resolve()


def save_storage(storage: dict, save_name: str = "storage.json"):
    """Save a dict as a JSON in the whatsappMessanger Folder

    Args:
        storage (dict): Storage of the browser
        save_name (str, optional): Name of the File. Defaults to "storage.json".
    """
    full_path = parent_folder.joinpath(save_name)
    with full_path.open(mode="w", encoding="utf8") as file:
        json.dump(storage, file)


def load_storage(save_name: str = "storage.json") -> Union[dict, None]:
    """Load a JSON to a Dict object that is saved befor with `save_storage`

    Args:
        save_name (str, optional): Name of the File. Defaults to "storage.json".

    Returns:
        Union[dict, None]: The deserilized JSON or None if the File was not found
    """
    full_path = parent_folder.joinpath(save_name)
    if not full_path.exists():
        return None
    with full_path.open(mode="r", encoding="utf8") as file:
        return json.load(file)


def print_qr_to_terminal_from_image(name: str, path: Path = Path.cwd()):
    """Print a QR Code from a terminal to the console

    Args:
        name (str): Name of the saved QR-Code
        path (Path, optional): Path of the `dir` to the file. Defaults to Path.cwd().
    """
    full_path = path.joinpath(name)
    data = decode(Image.open(full_path.absolute()))
    terminal_qr = pyqrcode.create(data[0].data)
    print(terminal_qr.terminal())
