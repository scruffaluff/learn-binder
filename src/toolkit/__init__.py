"""Personal workspace for learning Jupyter Binder integration."""


__author__ = "Macklan Weinstein"
__version__ = "0.1.0"


import numpy


def sawtooth() -> numpy.ndarray:
    """Computes an example sawtooth wave."""

    return numpy.array([-1 + (index % 200) / 100 for index in range(1_000)])
