"""Utility and example functions for calculating statistics."""


import numpy

from toolkit.typing import Samples


def mean(samples: Samples) -> float:
    """Calculate sample mean from a dataset."""

    # For a sequence of floats numpy.sum will return a float.
    return numpy.sum(samples) / len(samples)  # type: ignore
