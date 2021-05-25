"""Personal workspace for learning Jupyter Binder integration."""


__author__ = "Macklan Weinstein"
__version__ = "0.1.0"


import io
from typing import Tuple

from numpy.typing import ArrayLike
import requests
import soundfile


def download_audio(url: str) -> Tuple[ArrayLike, int]:
    """Fetch and load audio file from remote server."""

    response = requests.get(url)
    bytes = io.BytesIO(response.content)
    return soundfile.read(bytes)
