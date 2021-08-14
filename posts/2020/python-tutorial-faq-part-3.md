---
author: Julia Kent
date: 2020-11-18
tags: python-tutorial-series,faq,python
---

# Python Tutorial FAQ - Part 3

Here is a compilation of questions from the third session of the Python Tutorial Seminar Series which covered writing functions as well as f-string formatting.

---

**Q.** Seeing how `2/2` returns `1.0` instead of `1`, is the numeric type automatically determined from the inputs or do you have to force it?

**A.** The numeric type is inferred. `/` always returns a float for numeric types. `//` always returns an integer.

One should note that Python 2 does not behave this way. In Python 2, the `//` operator does not exist and the `/` operator behaves like it does in other languages (i.e., division of two integers yields an integer and division with a float yields a float).

---

**Q.** Are the spaces necessary around operators or after commas?

**A.** No it is not necessary, but it is best practice.

---

**Q.** What happens if you don’t explicitly specify a return value?

**A.** If you don’t want to return anything you don’t need to have a `return` statement at the end of your function. By default, that means the function will return `None`.

---

**Q.** Do functions have a specific location in the file?

**A.** Functions can be defined in any order. If you have a function above that calls a function defined below, it will work. But if you just call the function above its definition, it will fail. We recommend having a separate file that contains all the functions or helper functions - we will cover this in the “Your First Python Package” section.

---

**Q.** Do I have to worry about name clashing in global vs function scope? Would there be a problem if we used `t` and `v` for the names of our iterator variables in the for loop as well as the time and windspeed variables within the function?

**A.** In general, yes. If you create a variable in your function scope that has the same name as a variable in global scope, you will not be able to access the global scope variable from within the function. But everything would be fine in global scope.
In your example, however, it would be fine. The `t` and `v` variables in function scope will not overwrite the `t` and `v` (in your example) that are in global scope within the `for` loop.
You can access global scope variables from within a function.

---

**Q.** Will all the variables being created within a function still occupy the memory after the function was finished?

**A.** Python uses garbage collection for memory management. That means that those variables will no longer be referenced anywhere, so they will be cleaned up whenever garbage collection happens which is not necessarily after the function return or during the execution of your script as long as there is no reason to clear memory. Essentially garbage collection is complicated, and controlling memory with Python is a hard thing to do.

---

**Q.** In the `f-string` formatting (i.e., `f'string'`) is `f` a function?

**A.** No, it’s a special symbol before the string saying that it is an `f-string`. If you just had `‘’`, everything within the apostrophes would be a regular string. `f’’` is an `f-string`. `f-strings` in Python let you do nice string formatting.

---

**Q.** The `wc_data` and `wc_comp` are not defined. How does python know
what they refer to?

**A.** They are defined in the `for` loop and are returned from the `zip` function when it is iterated over.

---

**Q.** Can the loop `for wc_data, wc_comp in X` cause a memory leak?

**A.** It’s hard to create a memory leak with pure Python. `wc_data` is re-assigned every loop, overwriting the previous value and taking up the same amount of memory.

---

**Q.** Is there a difference between `‘` and `“` in strings?

**A.** No. You can use either, but you must be consistent within a given string in how you start and end it. This allows you to use the `’` character within your string, for example: `string = “I’m a string”`

---

**Q.** What is the meaning of `>6` in the time `f-string` formatting?

**A.** It means 6 characters in length, right justified.

---

**Q.** What is the meaning of `>6` in the time `f-string` formatting?

**A.** It means 6 characters in length, right justified.

---
