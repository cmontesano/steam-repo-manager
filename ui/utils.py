import os
from pathlib import Path
import requests
import glob
import webbrowser


def open_external(_, url: str = ''):
    webbrowser.open(url, new=0, autoraise=True)


def download_video(_, url: str):
    dest_path = os.path.join(Path.home(), '.steam', 'root', 'config', 'uioverrides', 'movies')

    # Ensure directory exists
    Path(dest_path).mkdir(parents=True, exist_ok=True)

    # Empty directory
    files = glob.glob(f"{dest_path}/*")
    for f in files:
        os.remove(f)

    response = requests.get(url)
    open(os.path.join(Path(dest_path), "deck_startup.webm"), "wb").write(response.content)
