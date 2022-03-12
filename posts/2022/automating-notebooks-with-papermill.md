---
author: Anderson Banihirwe, Matthew Long
date: 2022-03-11
tags: python, jupyter, notebooks, papermill, automation
---

# Automating Jupyter Notebooks with Papermill

Jupyter notebooks have revolutionized the way we analyze, document and share data science projects. Jupyter notebooks are really good for doing the heavy lifting of data analysis by:

- allowing you to showcase your work in a single place. You can see the complete "paper trail" of what was done. This includes the code, results, visuals and the narrative accompanying your analysis.

- allowing others to easily use your work as a starting point for their own analysis. A new user can run cell by cell through the notebook to better get an understanding of the code.

However, Jupyter notebooks have a few drawbacks:

- they are difficult to maintain and reuse. Unlike a regular Python module that you can import and use in any Python project, users are copying and pasting snippets from each other's notebooks, and it's very easy to get out of sync.
- they are hard to parameterize. This makes it difficult to maintain one version of the truth that can be used as a notebook template for exploring different parameters.

[**Papermill**](https://papermill.readthedocs.io/en/latest/) is a Python library that aims to solve some of these problems. Papermill allows users to run and parametrize Jupyter notebooks in a way that is easy to maintain and reuse. If you are a user who would like to run a notebook template with different input values (parameters), Papermill is the tool you need. In this blog post, we are going to share...
