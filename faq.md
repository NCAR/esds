# Frequently Asked Questions
This contains relevant questions and answers from common workflow issues and questions posted on Zulip.

## What do I do if my question is not answered on this page?

Open an issue [here](https://github.com/NCAR/esds/issues)

## Where do I go for help?

Try one of the following resources.
1. Xarray's [How Do I do X?](https://xarray.pydata.org/en/stable/howdoi.html) page
1. [Xarray Github Discussions](https://github.com/pydata/xarray/discussions)
1. [Pangeo Discourse Forum](https://discourse.pangeo.org)
1. NCAR Zulip under #python-questions, #python-dev, or #dask.

Avoid personal emails and prefer a public forum.

## Someone must have written the function I want. Where do I look?

See the xarray [ecosystem](https://xarray.pydata.org/en/latest/ecosystem.html) page. Also see the [xarray-contrib](https://github.com/xarray-contrib/) and [pangeo-data](https://github.com/pangeo-data) organizations. Some NCAR relevant projects include:
1. GeoCAT-comp
1. GeoCAT-viz
1. cf_xarray
1. climpred
1. eofs
1. MetPy
1. rechunker
1. xclim
1. xesmf
1. xgcm
1. pop-tools
1. xskillscore

## Where can I find Xarray tutorials?

See [videos](https://xarray.pydata.org/en/latest/tutorials-and-videos.html) and [notebooks](https://xarray-contrib.github.io/xarray-tutorial/).

## How do I debug my code when using dask? 

An option is to use `.compute(scheduler="single-threaded")`. This will run your code as a serial for loop. When an error is raised you can use the `%debug`
magic to drop in to the stack and debug from there. See [this post](https://cherian.net/posts/python-debugging.html) for more debugging tips
in a serial context.

## `KilledWorker` X{. What do I do?

Keep an eye on the dask dashboard. 
1. If a lot of the bars in the Memory tab are orange, that means your workers are running out of memory. Reduce your chunk size.

## Debugging conda environments

## Debugging the dask dashboard

### NCAR JupyterHub

### SSH tunnels to lab resources

## Help, my analysis is slow!

### General tips

1. Read the xarray documentation on [optimizing workflow with dask](https://xarray.pydata.org/en/stable/dask.html#optimization-tips).
1. Keep track of chunk sizes throughout your workflow. This is especially important when reading in data using `xr.open_mfdataset`. Aim for 100-200MB size
   chunks.
1. Choose chunking appropriate to your analysis. If you're working with time series then chunk more in space and less along time.
1. Avoid indexing with `.where` as much as possible. In particulate `.where(..., drop=True)` will trigger a compute since it needs
   to know where NaNs are present to drop them. Instead see if you can write your statement as a `.clip`,  `.sel`, `.isel`, or 
   `.query` statement.

### I have to do lots of rechunking, but the rechunk step uses too much memory and kills my workers.

Try the [rechunker package](https://github.com/pangeo-data/rechunker).

### Writing to files in parallel

Distributed writes to netCDF are hard.

1. Try writing to `zarr` using `Dataset.to_zarr`.
1. If you need to write to netCDF and your final dataset can fit in memory then use `dataset.load().to_netcdf(...)`.
1. If you really must write a big dataset to netCDF try using `save_mfdataset` (see [here](https://ncar.github.io/xdev/posts/writing-multiple-netcdf-files-in-parallel-with-xarray-and-dask/)). 
