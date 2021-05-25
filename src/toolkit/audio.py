"""Utility and example functions for using audio."""


import io
from typing import Tuple

from matplotlib import pyplot
from matplotlib.pyplot import Axes, Figure
from numpy.typing import ArrayLike
import requests
import soundfile

from toolkit.typing import Samples


def fetch(url: str) -> Tuple[Samples, int]:
    """Download and load audio file from remote server."""

    response = requests.get(url)
    bytes = io.BytesIO(response.content)
    return soundfile.read(bytes)


def plot(samples: ArrayLike) -> Tuple[Figure, Axes]:
    """Plot multiple channels of audio."""

    figure, axes = pyplot.subplots(dpi=200, figsize=(12, 4))
    axes.plot(samples)

    axes.set_xlabel("Index")
    axes.set_ylabel("Amplitude")
    axes.set_ylim(-1, 1)

    return figure, axes
