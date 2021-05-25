"""Utility and example functions for calculating statistics."""


import numpy

from toolkit.typing import Samples


def mean(samples: Samples) -> float:
    """Calculate sample mean from a dataset."""

    return numpy.sum(samples) / len(samples)
