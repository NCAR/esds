---
author: Julia Kent
date: 2021-02-19
tags: python-tutorial-series,faq
---

# Your First Package Python Tutorial FAQ

Here is a compilation of questions from the fourth and fifth sessions (["Your First Package"](https://ncar.github.io/python-tutorial/tutorials/yourfirst.html#first-python-package)) of the Python Tutorial Seminar Series which covered refactoring code into seperate modules and packages, using an external built-in module (`math`), and how to publish your package

---

**Q.** Should we add `__init__.py` to `.gitignore`?

**A.** We do not advise that. `__init__.py` is a special file that needs to be in that directory for Python to know to treat that directory like a Python package. So you need it even though it is, in this case, an empty file.

Whenever you do an import of a module, that module is executed. So if you’ve defined variables or run code in that file - at import time, that code will be executed. Modules tend to only contain function definitions or the construction of data or classes, so that at import time these definitions are available to us without. `__init__.py` works much the same way. Whenever you import something from a package its `__init__.py` will be executed. Since we don’t need anything done, in our situation, it is empty.

---

**Q.** Why do we use `touch` to create the file?

**A.** When you specify the name of the file to be edited, often times your text editor will automatically generate a file with that name if it does not already exist. So `touch` is not strictly necessary, but when creating `__init__.py` which is an empty file, we can see how `touch` is convenient.

---

**Q.** Is there a standard list of available Python packages that includes their functionality?

**A.** There isn’t any ONE place, but Python Package Index (PyPiI) is the canonical place to publish. Most packages have an install on PyPI and pypi.org is searchable by name, description, category, etc.

---

**Q.** Will `pip install …` ever choke based on my Conda version?

**A.** No, it won’t. Pip will look for and try to install from PyPI. If your Pip install is tied to a specific version of Python, and you try to install a package tied to a different version - the install will fail. You could have multiple Conda environments, each with a different Python version installed on them, and subsequently each with a different Pip version as well. Pip is not tied to Conda, but it is tied to Python (and we used Conda to install Python).

---

**Q.** Is my Conda environment tied to my directory?

**A.** No it is not, they just happen to have the same name because they are the same project. You could use the same conda environment for multiple directories if you wanted to.

---
