---
author: Max Grover
date: 2021-4-9
tags: dask, intake, cesm
---

# An Example of Using Intake-ESM

This past week, NCAR CISL updated the Casper Node to use PBS instead of Slurm for scheduling jobs. This led a post in which an example of spinning up dask clusters on the new configuration. This was also an opportunity to dig into dask, and try applying it to a sample task, specifically looking at ecosystem variables in the CESM-LE dataset, using notebooks included in Matt Long's [krill-cesm-le repository](https://github.com/matt-long/krill-cesm-le), modified by Kristen Krumhardt.

## Setting up the imports/dask

```python
%matplotlib inline
import os
import shutil

from glob import glob

import cftime

import numpy as np
import xarray as xr

import matplotlib.pyplot as plt
import matplotlib.colors as colors

import cartopy.crs as ccrs
from cartopy.util import add_cyclic_point

import intake
import pop_tools
import esmlab
import util

import warnings
warnings.filterwarnings('ignore')
```

### Spin up Dask Cluster

Here, we spin up our dask cluster. At first, running this notebook resulted in a `killed worker` error. After further expection, we noticed that additional resources would be needed to read in the notebook since the data are so large (on the order of ~1-2 TB). Increasing the individual worker to a higher amount (ex. 256 GB) solved the issue. Scale up to as many workers as you think are neccessary for the calculation (this may take some trial and error).

You should base your chunks on your analysis - so in this case, we are interested in the top 100 m in the ocean, so chunking by `z_t`, the vertical coordinate, will help reduce the memory.

Good general advice for working with dask is to check the dask graph (accessed via the url when you call the client). When there are "orange" regions within your task graph, this means your workers are getting close to maxing out on memory.

```python
import dask

# Use dask jobqueue
from dask_jobqueue import PBSCluster

# Import a client
from dask.distributed import Client

# Setup your PBSCluster
cluster = PBSCluster(
    cores=2, # The number of cores you want
    memory='256 GB', # Amount of memory
    processes=1, # How many processes
    queue='casper', # The type of queue to utilize (/glade/u/apps/dav/opt/usr/bin/execcasper)
    local_directory='$TMPDIR', # Use your local directory
    resource_spec='select=1:ncpus=2:mem=256GB', # Specify resources
    project='project_id', # Input your project ID here
    walltime='02:00:00', # Amount of wall time
    interface='ib0', # Interface to use
)
# Scale up
cluster.scale(4)

# Change your url to the dask dashboard so you can see it
dask.config.set({'distributed.dashboard.link':'https://jupyterhub.hpc.ucar.edu/stable/user/{USER}/proxy/{port}/status'})

# Setup your client
client = Client(cluster)
```

## Read the CESM-LE data

We will use [`intake-esm`](https://intake-esm.readthedocs.io/en/latest/), which is a data catalog tool.
It enables querying a database for the files we want, then loading those directly as an `xarray.Dataset`.

First step is to set the "collection" for the CESM-LE, which depends on a json file conforming to the [ESM Catalog Specification](https://github.com/NCAR/esm-collection-spec).

```python
catalog_file = '/glade/u/home/kristenk/TTE_CESM-LE/krill-cesm-le/notebooks/data/glade-cesm1-le.json'
variables = ['TEMP', 'diatC']

experiments = ['20C', 'RCP85']
stream = 'pop.h'

col = intake.open_esm_datastore(catalog_file)
```

Now we search the collection for the ensemble members (unique `member_id`'s) that have a chlorophyll field (`diatChl`). This is necessary because the ocean biogeochemistry was corrupted in some members and the data were deleted.

In this cell, `member_id` is a list of the ensemble members we want to operate on.

```python
col_sub = col.search(experiment=['20C'],
                     stream='pop.h',
                     variable=['diatChl'])

member_id = list(col_sub.df.member_id.unique())
print(member_id)
```

### Apply the search for data

Specify a list of variables and perform a search. Under the hood, the `search` functionality uses [`pandas`](https://pandas.pydata.org/) data frames. We can view that frame here using the `.df` syntax.

```python
col_sub = col.search(
    experiment=experiments,
    stream=stream,
    variable=variables,
    member_id=member_id,
    )

print(col_sub)

col_sub.df.head()
```

Use `.to_dataset_dict` to read in the datasets as a dictionary, specifying the chunk size. This is also a point where it is recommended you take a look at the `chunksize` for the dask array, ensuring that it is a reasonable number (~100-200 mb). Test it out on one of the variables (ex. `TEMP`).

Since we are only interested in the top 100 m, we can chunk by `z_t` by 10 which should reduce the memory usage.

```python
dsets = col_sub.to_dataset_dict(cdf_kwargs={'chunks': {'time':5, 'z_t':10}, 'decode_times': False})
```

## Apply an operation

Apply a calculation. In this case, we are calculating the average temperature within the top 100 m of the ocean.

```python
def compute_TEMP_100m(ds):
    """compute top 100m mean temperature"""

    ds['TEMP_100m_mean'] = ds.TEMP.isel(z_t=slice(0,10)).mean(dim='z_t')
    ds.TEMP_100m_mean.attrs = ds.TEMP.attrs
    ds.TEMP_100m_mean.attrs['long_name'] = 'Mean temperature over top 100m'

    return ds.drop(['TEMP'])
```

Now apply this function to the dataset(s)

```python
# compute top 100m temperature
dsets2 = {key: compute_TEMP_100m(ds) for key, ds in dsets2.items()}
print('computed top 100m temp')
```

### Combine the datasets

Concatenate the datasets in time, i.e. 20C + RCP8.5 experiments.

```python
ordered_dsets_keys = ['ocn,20C,pop.h', 'ocn,RCP85,pop.h']
#ordered_dsets_keys = ['ocn.20C.pop.h', 'ocn.RCP85.pop.h']
ds = xr.concat(
    [dsets2[exp] for exp in ordered_dsets_keys],
    dim='time',
    data_vars='minimal',
    #compat='override' ## added this
)
time_encoding = dsets2[ordered_dsets_keys[0]].time.encoding
```

### Calculate an annual mean

Create an annual mean for temperature, using a [utility function](https://github.com/matt-long/krill-cesm-le/blob/master/notebooks/util.py#L185) which deals with the times correctly.

```python
ds_ann = util.ann_mean(ds, time_bnds_varname='time_bound', time_centered=True)
```

## Write the dataset to disk

Here, we are just looking to write out a few of the variables.

```python

# Create a list of variables to write out
keep_vars = ['time_bound', 'TAREA', 'time', 'dz', 'KMT', 'member_id', 'TLAT', 'TLONG', 'TEMP_100m_mean']

# Subset for these variables
ds_out = ds_ann[keep_vars])

# Run the computations
ds_out.compute()

# Write out to scratch since this is likely a large file
ds_out.to_netcdf('/glade/scratch/username/CESM-LE-output/CESM-LE-TEMP_100m_mean.nc')
```

While this is a rather specific example, I hope this illustrates how useful [intake-esm](https://github.com/intake/intake-esm) can be and the power of [dask](https://docs.dask.org/en/latest/) for computing these computationally expensive calculations on large datasets.
