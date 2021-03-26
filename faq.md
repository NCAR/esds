# Frequently Asked Questions
This contains relevant questions and answers from common workflow issues and questions posted on Zulip.

***This page is meant to be a list of FAQ regarding climate datasets, movivated by a variety of employees across UCAR/NCAR***


## How do I optimize reading multiple files using Xarray and Dask?

### I receive errors when trying to read in my dataset... are there certain arguements

A good first place to start when reading in multiple files is [Xarray's multi-file documentation](https://xarray.pydata.org/en/stable/io.html#reading-multi-file-datasets).

For example, if you are trying to read in multiple files where you are interested in concatenating over the time dimension, here is an example of the `xr.open_dataset` line would look like:

```python
ds = xr.open_mfdataset(
        files,
        # Name of the dimension to concatenate along.
        concat_dim="time",

        # Attempt to auto-magically combine the given datasets into one by using dimension coordinates.
        combine="by_coords",

        # Specify chunks for dask - explained later
        chunks={"lev": 1, "time": 500},

        # Only data variables in which the concat_dim already appears are concatenated.
        data_vars="minimal",

        # Only coordinates in which the dimension already appears are included.
        coords="minimal",

        # Skip comparing and pick variable from first dataset.
        compat="override",
        parallel=True,
    )
```

### My file is taking forever to read in... what can I do to improve this?

1. Try subsetting for ***just*** the variable(s) you need for example, if you are reading in a dataset with ~25 variables, and you only need `temperature`, just read in temperature. You can specificy which variables to read in by using the following syntax, following the example of the temperature variable.

```python
ds = xr.open_dataset(file, data_vars=['temperature'])
```

1. Your chunk size, using Dask, is not optimized. When reading a file in using Xarray with Dask, a "general rule of thumb" is to keep your chunk size down to around 100 mb.

For example, let's say you trying to read in multiple files, each with ~600 time steps. This is case where each file is very large (several 10s of GB) and using Dask to help with data processing is *essential*.

You can check the size of each chunk by subsetting a single DataArray (ex. `ds['temperature']`)

If you have very large chunks, try modifying the number of chunks you specify within  `xr.open_mfdataset(files, ..., chunks={'lev':1, "time": 500})` where lev and time are vertical and time dimensions respectively.

Check to see how large each chunk is after modifying the chunk size, and modify as necessary.

1. You do not have enough dask workers

If you have a few large files, having the number of workers equal to to the number of input files read in using `xr.open_mfdataset` would be a good practice

If you have a large number of smaller files, you may not run into this issue, and it is suggest you look at the other potential solutions.
