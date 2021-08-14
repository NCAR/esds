---
author: Julia Kent
date: 2020-11-05
tags: python-tutorial-series,faq,python
---

# Python Tutorial FAQ - Part 2

Here is a compilation of questions and issues that arose during the second session of the Python Tutorial Seminar Series, on creating a data dictionary. After this first short series, these FAQ sections will be added to the [Xdev tutorial website](https://ncar.github.io/python-tutorial/)

---

**Q.** Why is `list[0:10]` the first 10 elements, not 11?

**A.** In Python, "list slicing" uses square brackets with the syntax `[start:stop:step]`. The `start` is _inclusive_, while the `step` is _exclusive_. So, you read up to (but excluding) the `stop` index.

---

**Q.** Why do we not say `list[1,10]` to return the first 10 elements?

**A.** Python is 0-indexed, so index of 1 actually refers to the second element. Say our list was `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]`, then `list[1,10]` would return `[1, 2, 3, 4, 5, 6, 7, 8, 9]` (which is missing the first element) and `list[0,10]` returns the desired `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]` (Also, see the answer to the previous question).

---

**Q.** So `list[0:1]` is just one value, same as `list[0]`?

**A.** Actually not. `list[0:1]` returns a list, due to the slice indexing, with a value of `[0]`, whereas `list[0]` returns the 0th element, and has a value of `0`. Notice the square brackets or their absence!

---

**Q.** How do you read only the 1st, 4rd, 7th, 10th, . . . rows of a data?

**A.** Using `list[::3]`

---

**Q.** Could you clarify how this part works again:

```
# Read the first three lines (header)
for _ in range(3):
    datafile.readline()
```

**A.** `range(3)` is an iterator; it is equivalent to using the list `[0,1,2]`. Here we’re iterating over that 3-element list and using the value for each iteration as the value of the variable `_`. (We need to define the variable `_` in order to iterate through the for-loop, but we never use it, which is why we just call it `_`.). In every iteration, we call `datafile.readline()` which means we read 3 lines of text from the file _in total_, but since we aren’t saving those lines of text anywhere (i.e., in any variable) we are only reading and discarding them. (Note, anything that begins with an underscore is generally considered "discardable" by common practice, but there is no rule in Python about that.) This for-loop sets us up so the next `readline()` call is where the data values begin.

---

**Q.** Why is there no `end for` in a Python for-loop?\n",

**A.** Python is sensitive to white space. Anything indented after the `for` statement is part of the for-block, everything else after that is after the for-loop has completed. There is no extra information that an `end for` line would be needed to convey.

---

**Q.** Why do we initialize data as an empty list with `data = []`?

**A.** If we want to use the `append` function to add elements to our list, the object to which we’re adding elements to has to be an _existing_ (i.e., initialized) list.

---

**Q.** Why do you refer to the data dictionary elements using `[]` when it is not a list?

**A.** Square brackets, `[]`, are used in Python to _declare a list_ and to _get an item_. In the "get item" usage, the square brackets must be preceded by the name of the variable from which the item is being retrieved. In the list declaration usage, the square brackets must exist _alone_ (i.e., no variable name preceding it). For example, `x[0]` means "get element `0` from `x`" and `[0]` (i.e., without the `x` in front) means "create a list containing the element `0`". The "declare a list" syntax is obviously _only_ for creating a list, but the "get item" syntax can be used with _any container_ (i.e., lists, dictionaries, sets, etc.). (**NOTE:** Slice notation, namely `x[start:stop:step]`, only works on lists, and it does not work with dictionaries or sets!)

---

**Q.** How do you print a single element from a variable, like `tempout`, from the data dictionary?

**A.** `data['tempout'][9]`

---

**Q.** Could you explain more about function pointers?

**A.** Everything in Python is an object. You may be used to passing around variables by reference or value. In Python you can also pass around a function without calling it. In this session we passed in `float` which is a class of objects - and can also be used like a function. We stored the name of the function in the types dictionary so that we could use the function later on in the code.

---
