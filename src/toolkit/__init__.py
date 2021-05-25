"""Personal workspace for learning Jupyter Binder integration."""


__author__ = "Macklan Weinstein"
__version__ = "0.1.0"


import io
from typing import Tuple

from matplotlib import pyplot
from matplotlib.pyplot import Axes, Figure
from numpy.typing import ArrayLike
import requests
import soundfile


def download_audio(url: str) -> Tuple[ArrayLike, int]:
    """Fetch and load audio file from remote server."""

    response = requests.get(url)
    bytes = io.BytesIO(response.content)
    return soundfile.read(bytes)  # type: ignore


def plot_audio(samples: ArrayLike) -> Tuple[Figure, Axes]:
    """Plot multiple channels of audio."""

    figure, axes = pyplot.subplots(dpi=200, figsize=(12, 4))
    axes.plot(samples)

    axes.set_xlabel("Index")
    axes.set_ylabel("Amplitude")
    axes.set_ylim(-1, 1)

    return figure, axes
