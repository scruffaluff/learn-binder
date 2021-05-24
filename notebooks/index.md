# Learn Binder

Welcome to Learn Binder. It is a personal workspace for me to learn Jupyter
Binder integration with GitHub repositories. I hope that it will render math
documentation such as $x^2 = 3$.

Here are some Jupyter keyboard commands for reading this book. The basic way to
read the book is start at the top of each chapter and run each cell by pressing
<kbd>Shift</kbd>+<kbd>Enter</kbd>. When you run a Code cell, the result will be
printed below the cell. For more information about how to use these Juptyer
notebooks, see the top pulldown menus.

| Keyboard Command | Action |
|-------------:|---------------|
|<kbd>Shift</kbd>+<kbd>Enter</kbd> | Run the selected Jupyter cell and advance to the next cell |
|<kbd>Ctrl</kbd>+<kbd>Enter</kbd> | Run the selected Jupyter cell and don't advance |
|<kbd>Alt</kbd>+<kbd>Enter</kbd> | Run the selected Jupyter cell and insert a new cell after |
|<kbd>Enter</kbd> | Edit the selected Jupyter cell |
|<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>-</kbd> | Split the Jupyter cell at the cursor position |

```python
from matplotlib import pyplot
import numpy

array = numpy.linspace(0, 5, 100)
pyplot.plot(array)
```

```python
import learn_binder

pyplot.plot(learn_binder.sawtooth())
```
