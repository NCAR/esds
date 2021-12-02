---
author: Max Grover
date: 2021-12-02
tags: update, faq, xarray, dask, matplotlib
---

# ESDS Update October 2021

November was an active month! There were a variety of talks, a variety of answered Python questions during office hours, and a Python tutorial!

Check out the following ESDS update for the month of November 2021.

## Xdev Updates

Xdev has made some important advances on [`Intake-ESM`](https://intake-esm.readthedocs.io/en/latest/), which is a data catalog utility comprising an API to data assets. Essentially, intake-esm "abstracts away" the file system, enabling data search and discovery, automated queries and dataset construction, and portability across cloud and HPC platforms. We're now working on a set of ideas we're calling **_Funnel_**; this extends the data catalog with "analysis recipes", providing an effective strategy for modularization and extensibility of workflows.

We also held our first discussion on `xwrf`, which is a new package meant to bring Weather Research and Forecasting (WRF) data into the Pangeo Ecosystem! Using this tool, users can read WRF output directly into `Xarray`, enabling the use of `Dask` and `hvPlot`. If you are interested in following along with that development, be sure to check out the [`xwrf` repository](https://github.com/NCAR/xwrf).

## ESDS Forum

### Python Package Overviews

- [Introducing Project Raijin Community Geoscience Analysis Tools for Unstructured Mesh Data](https://raijin.ucar.edu/) (29 November 2021) - Orhan Eroglu (CISL)

### General Discussion

- [An Open Discussion Around Earth System Prediction at NCAR](https://docs.google.com/forms/d/e/1FAIpQLScX4ugyocLz1WgIthzX_eN_CXkBR7QvlHTS0eMLxFtxsjxPyw/viewform?vc=0&c=0&w=1&flr=0) (01 November 2021) - Matt Long (CGD)

## ESDS Blog Posts

### Data Computation

- [Correctly Calculating Annual Averages with Xarray](https://ncar.github.io/esds/posts/2021/yearly-averages-xarray/)

### End to End Workflow

- [Processing Data from the NCAR Mesa Lab Weather Station¶](https://ncar.github.io/esds/posts/2021/weather-station-data-preprocess/)

## Office Hour Questions

During the month of October 2021, our team answered a total of **10 questions** at our weekly [Xdev Office Hours](https://ncar.github.io/esds/calendar/#xdev-office-hours).

Below is a summary of the most common questions brought up during office hours!

![october-2021-office-hours](../images/october_2021_question_topics.png)

### Matplotlib Questions

- ## How do you make boxplots with two datasets of varying sizes?

### Dask Questions

- ## How do you run Dask on Casper?

### Xarray Questions

- ## How do you load multiple files into xarray and plot the output?
- ## How do you drop specific dates from a dataset?

### Conda Questions

- ## How do you uninstall and reinstall a conda environment?
- ## How do you make sure your conda environment is activated upon opening terminal?

## Python Tutorial(s)

### [Object Oriented Programming Tutorial](https://ncar.github.io/esds/posts/2021/oop-tutorial/)

<iframe width="560" height="315" src="https://www.youtube.com/embed/zlHkkjr7e6k" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
