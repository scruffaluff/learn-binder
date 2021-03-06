"""Utility and example functions for using audio."""


import io
from typing import Tuple

from bokeh import plotting, resources
import bokeh.io
from matplotlib import pyplot
import numpy
from plotly import express, graph_objects
import requests
import soundfile

from toolkit.typing import Samples


def fetch(url: str) -> Tuple[Samples, int]:
    """Download and load audio file from remote server."""

    response = requests.get(url)
    bytes = io.BytesIO(response.content)
    # Since an out argument was not passed to the method, it is guaranteed to
    # return a Numpy array and an integer sample rate.
    samples, rate = soundfile.read(bytes, always_2d=True)  # type: ignore
    return numpy.average(samples, axis=1), rate


def chart_bokeh(samples: Samples) -> plotting.Figure:
    """Plot single channel of audio samples with Bokeh."""

    bokeh.io.output_notebook(hide_banner=True, resources=resources.INLINE)
    figure = plotting.figure(
        plot_height=320,
        plot_width=920,
        x_axis_label="Sample",
        x_range=(0, len(samples)),
        y_axis_label="Amplitude",
        y_range=(-1.0, 1.0),
    )
    figure.line(numpy.arange(len(samples)), samples)

    bokeh.io.show(figure)
    return figure


def chart_plotly(samples: Samples) -> graph_objects.Figure:
    """Plot single channel of audio samples with Plotly."""

    figure = express.line(
        height=320,
        range_x=(0, len(samples)),
        range_y=(-1.0, 1.0),
        width=920,
        y=samples,
    )
    figure.update_layout(
        xaxis_title="Sample",
        yaxis_title="Amplitude",
    )

    figure.show()
    return figure


def chart_pyplot(samples: Samples) -> Tuple[pyplot.Figure, pyplot.Axes]:
    """Plot single channel of audio samples with PyPlot."""

    figure, axes = pyplot.subplots(dpi=200, figsize=(6, 1.75))
    axes.plot(samples)

    axes.set_xlabel("Sample")
    axes.set_xlim(0, len(samples))
    axes.set_ylabel("Amplitude")
    axes.set_ylim(-1, 1)

    return figure, axes
