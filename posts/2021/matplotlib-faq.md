---
author: Julia Kent
date: 2021-03-30
tags: python-tutorial-series,faq,matplotlib
---

# Matplotlib Tutorial FAQ

Here is a compilation of questions and issues that arose during the [Matplotlib](https://www.youtube.com/watch?v=EiPRIdHQEmE) session of the Python Tutorial Seminar Series.

---

**Q.** Are all the colormaps perceptually ordered?

**A.** They are not all perceptually ordered. Any color map you can think of exists or can be made. The [Matplotlib Documentation](https://matplotlib.org/stable/tutorials/colors/colormaps.html) has a good guide for choosing colormaps.

---

**Q.** How do you set the x-axis boundary to remove the padding left and right of where the data begins/ends?

**A.** You would use `ax.set_xlim` and provide the minimum and maximum x-values as input. You can infer these from your `x` data with the full command `ax.set_xlim([min(x), max(x)])`.

---

**Q.** How do you create a .png from a notebook?

**A.** You can save a figure by running `plt.savefig(‘filename.png’)` in the cell you plotted the figure. The file type is inferred from the filename. `png`, `pdf`, `ps`, `eps`, `jpg`, and `svg` are all supported image formats on most backends.

---

**Q.** How can we set resolution (dpi) when saving plots?

**A.** `dpi` is a keyword argument to `savefig`. So you can call `plt.savefig(FIGURENAME.EXT, dpi=FLOAT)` where you specify your desired dots per inch as a float.

---

**Q.** How can I add a shared colorbar for the subplots?

**A.** There are many of examples of how to do this in the GeoCAT-examples documentation. [Here](https://geocat-examples.readthedocs.io/en/latest/gallery/Contours/NCL_eof_1_1.html#sphx-glr-gallery-contours-ncl-eof-1-1-py) is an example that does so while plotting EOFs of the Sea Level Pressure over the North Atlantic. The [Matplotlib documentation](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/colorbar_placement.html) also has great instructions on how to manipulate colorbars.

---
