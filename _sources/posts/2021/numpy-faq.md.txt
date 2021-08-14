---
author: Julia Kent
date: 2021-03-19
tags: python-tutorial-series,faq,numpy
---

# NumPy Tutorial FAQ

Here is a compilation of questions and issues that arose during the [Numpy](https://colab.research.google.com/drive/1zcjaGXofLzUXkQzJKnANE9Z3yFUt0q7E?usp=sharing) session of the Python Tutorial Seminar Series.

The live video recording of this content can be found [here](https://www.youtube.com/watch?v=kstc-6uz7AQ&t=10s).

---

**Q.** Is it possible to provide a “step” instead of a number of elements when using `numpy.linspace` to create an array?

**A.** The step size is derived from the input arguments `start`, `stop`, and `number` with `numpy.linspace`. If you instead want to supply the step size and derive the number of steps, you would instead use the function `numpy.arange` that takes the input arguments `start`, `stop`, and `number`. `numpy.arange()` differs from Python’s built-in `range()` function which only supports integers and produces a `list` rather than an `array`.

---

**Q.** Are there Python methods that mutate the object, or do they always generate a new object? If so, are there any good heuristics for knowing which methods change their objects and which generate changed copies?

**A.** Yes there are Python functions that mutate the object. Checking the documentation is the safest way to confirm how the functions from library or package behaves.

---

**Q.** Is it faster to work with a Python `list` or a Numpy `array`?

**A.** Arrays are faster if you want to modify the object. You can test which is faster in a Jupyter notebook by typing `%%time` at the top of your cells, or `%%timeit` which will run the cell multiple times and produce the average time of computation.

---

**Q.** Can numpy Arrays hold non-numeric data?

**A.** Yes, a Numpy `array` can hold any data type of equivalent size as well as any Numpy native data type. It cannot hold varying like `string`s, but `string`s of the same lengths are acceptable. All of the elements of a Numpy `array` must be the same type as each other.

---
