---
jupyter:
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

# Statistics

## Table of Contents

- [Preface](./nteract/edit/notebooks/index.ipynb)
- [Chapter 1: Basics](./nteract/edit/notebooks/chapter_1.ipynb)

## Jupyter

Here are some Jupyter keyboard commands for reading this book. The basic way to
read the book is start at the top of each chapter and run each cell by pressing
<kbd>Shift</kbd>+<kbd>Enter</kbd>. When you run a Code cell, the result will be
printed below the cell. For more information about how to use these Juptyer
notebooks, see the top pulldown menus.

|               Keyboard Command                | Action                             |
| :-------------------------------------------: | ---------------------------------- |
|       <kbd>Shift</kbd>+<kbd>Enter</kbd>       | Run cell and advance to next cell  |
|       <kbd>Ctrl</kbd>+<kbd>Enter</kbd>        | Run cell and don't advance         |
|        <kbd>Alt</kbd>+<kbd>Enter</kbd>        | Run cell and insert new cell after |
|               <kbd>Enter</kbd>                | Edit cell                          |
| <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>-</kbd> | Split cell at cursor position      |

### Examples

Most audio files are from [SoundCamp](https://soundcamp.org/).

```python
from IPython import display
from matplotlib import pyplot
import toolkit.audio

url = "https://soundcamp.org/sounds/381/snare/A/clean-snare-sample-a-key-06-oV5.wav"
samples, rate = toolkit.audio.fetch(url)

toolkit.audio.chart_bokeh(samples)
toolkit.audio.chart_pyplot(samples)
display.Audio(samples.T, rate=rate)
```
