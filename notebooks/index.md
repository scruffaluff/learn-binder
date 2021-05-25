# Learn Statistics

Welcome to Learn Binder. It is a personal workspace for me to learn Jupyter
Binder integration with GitHub repositories. I hope that it will render math
documentation such as $x^2 = 3$.

Here are some Jupyter keyboard commands for reading this book. The basic way to
read the book is start at the top of each chapter and run each cell by pressing
<kbd>Shift</kbd>+<kbd>Enter</kbd>. When you run a Code cell, the result will be
printed below the cell. For more information about how to use these Juptyer
notebooks, see the top pulldown menus.

|                              Keyboard Command | Action                                                     |
| --------------------------------------------: | ---------------------------------------------------------- |
|             <kbd>Shift</kbd>+<kbd>Enter</kbd> | Run the selected Jupyter cell and advance to the next cell |
|              <kbd>Ctrl</kbd>+<kbd>Enter</kbd> | Run the selected Jupyter cell and don't advance            |
|               <kbd>Alt</kbd>+<kbd>Enter</kbd> | Run the selected Jupyter cell and insert a new cell after  |
|                              <kbd>Enter</kbd> | Edit the selected Jupyter cell                             |
| <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>-</kbd> | Split the Jupyter cell at the cursor position              |

## Chapters

[Chapter 1](/nteract/edit/notebooks/chapter_1.md)

```python
from IPython import display
from matplotlib import pyplot
import io
import librosa
import numpy
import requests
import soundfile
import toolkit

array = numpy.linspace(0, 5, 100)
pyplot.plot(array)
```

```python
pyplot.plot(toolkit.sawtooth())
```

This is an extra text block.

```python
response = requests.get("https://soundcamp.org/sounds/381/snare/A/subtle-reverb-snare-drum-sound-a-key-01-Kb6.wav")
bytes = io.BytesIO(response.content)
buffer, sample_rate = soundfile.read(bytes)
```

```python
pyplot.plot(buffer)
```

```python
display.Audio(buffer.T, rate=sample_rate)
```
