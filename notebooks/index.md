# Learn Binder

Welcome to Learn Binder. It is a personal workspace for me to learn Jupyter
Binder integration with GitHub repositories. I hope that it will render math
documentation such as $x^2 = 3$.

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
