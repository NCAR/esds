---
author: Matt Long
date: 2021-4-22
tags: xarray, dask, pop
---

# How to Use `xarray.map_blocks` within a Mixed-Layer Depth Calculation

Within this example, we cover how to use `xarray.map_blocks` to calculate the mixed-layer depth within CESM POP model output.

This calculation is "embarassingly parellel" such that each calculation is done within a single a column. The calculation ***should*** be easily computed within each column across the model domain. This is where `map_blocks` can be used to improve the performance of this metric.

## Imports and Data Ingestion

We use the following libraries/packages within this example
```python
import os

from scipy import interpolate
import numpy as np
import xarray as xr

import matplotlib.pyplot as plt

import pop_tools
```

Next, we read in the data using `xarray` and subset for temperature and salinity, subsetting for a smaller portion of the domain for testing purposes

```
ds = xr.merge((
    xr.open_dataset('/glade/p/cgd/oce/projects/cesm2-marbl/xpersist_cache/3d_fields/TEMP-presentday-monclim.nc'),
    xr.open_dataset('/glade/p/cgd/oce/projects/cesm2-marbl/xpersist_cache/3d_fields/SALT-presentday-monclim.nc'),    
))


ds = ds[['TEMP', 'SALT']]

# subset for testing purposes
ds = ds.isel(member_id=slice(0, 2), nlat=slice(2, 5), nlon=slice(1, 5)) 
```

## Data Operation
Next, we setup a function to compute mixed layer depth using a difference in density (sigma)

```python
def mld_dsigma(SALT, TEMP, dsigma=0.03, rho_chunks={'nlat': 16, 'nlon': 16}):
    """
    Compute MLD based on ∆σ criterion. Uses xarray.map_blocks.
    
    Parameters
    ----------
    
    SALT : xarray.DataArray
      Salinity
    TEMP : xarray.DataArray
      Potential temperature
    dsigma : float, optional
      The value for ∆σ.
      
    Returns
    -------
    
    MLD : xarray.DataArray
      The MLD (m) defined as the point in the water column where
      density exceeds rho[0] + dsigma.      
    """
    
    # determine dimensionality
    dims_in = SALT.dims
    assert dims_in == TEMP.dims, 'dimension mismatch'
    assert 'z_t' in SALT.coords, 'z_t not found in SALT coords'

    # drop ancillary coordinates (this may not be necessary)
    SALT = SALT.reset_coords(drop=True)
    TEMP = TEMP.reset_coords(drop=True)
    
    # compute density
    rho = pop_tools.eos(SALT.chunk({'z_t': 10}), 
                        TEMP.chunk({'z_t': 10}), 
                        depth=SALT.z_t * 0.).compute()
    
    # add these coordinates which creep in somewhere, I think when xarray does the unstack
    # without these, I get an error: not expecting {'nlat', 'nlon'}
    # chunking here is arbitrary and maybe suitable for the global POP_gx1v7 grid
    if 'nlat' in rho.dims and 'nlon' in rho.dims:
        rho = rho.assign_coords({
            'nlat': xr.DataArray(np.arange(len(SALT.nlat)), dims=('nlat')),
            'nlon': xr.DataArray(np.arange(len(SALT.nlon)), dims=('nlon')),
        })
        
    rho = rho.chunk(rho_chunks).persist()
    
    # compute and return MLD - this is where the parallelization comes in
    return xr.map_blocks(
        interp_mld_dsigma, rho,
        kwargs=dict(dsigma=dsigma), 
        template=rho.isel(z_t=0).drop('z_t'),
    )
```

### Applying Mixed Layer Depth Calculation
This function, `interp_mld_dsigma` is designed to be called within `xr.map_blocks`. It assumes that `rho_in` has a depth dimension, `z_t` and some number of unspecified other dimensions, `non_vertical_dims`.

The non_vertical_dims are "stacked" using `xarray.stack` and the code loops over these dimensions, performing linear interpolation in `z_t` at each location.

The data are return unstacked with the dimensions ordered as the arrived in `rho_in`.

We define the function here, then immediately call it to test it; arbitrarily, we're calling it on TEMP rather than density.

```python
def interp_mld_dsigma(rho_in, dsigma=0.03):
    """compute MLD at point using interpolation"""
    
    # TODO: this will probably fail if non_vertical_dims = []
    #       In that case, we might use `expand_dims` to add a dummy dimension
    non_vertical_dims = [d for d in rho_in.dims if d not in ['z_t']] 
    rho_stack = rho_in.stack(non_vertical_dims=non_vertical_dims)
    mld_stack = xr.full_like(rho_stack.isel(z_t=slice(0, 1)), fill_value=np.nan)
    N = len(rho_stack.non_vertical_dims)
    z_t = rho_in.z_t * 1e-2
    
    for i in range(N):
        # if all NaN, skip this column
        if np.isnan(rho_stack[:, i]).all():
            continue

        # if the whole column has density less than the threshold, set MLD to deepest point
        if (rho_stack[:, i] < rho_stack[0, i] + dsigma).all():
            k = np.where(~np.isnan(rho_stack[:, i]))[0]
            mld_stack[:, i] = z_t[k[-1]]
        
        # linearly interpolate
        else: 
            f = interpolate.interp1d(
                rho_stack[:, i], z_t, 
                assume_sorted=False,
            )
            mld_stack[:, i] = f(rho_stack[0, i] + dsigma)

    return mld_stack.unstack().isel(z_t=0, drop=True).transpose(*non_vertical_dims)

# simulate what happens in map_blocks
subset_to_singletons = dict(nlat=slice(0, 1), nlon=slice(0, 1), member_id=slice(0, 1), month=slice(0, 1))

dsigma=0.5
temp_depth = interp_mld_dsigma(ds.TEMP.isel(subset_to_singletons).reset_coords(drop=True), dsigma=dsigma)
```

## Visualize the Output
Here's a plot of the MLD diagnosed using TEMP by the linear interpolation method above.

```python

plt.figure(figsize=(4, 6))

ds.TEMP.isel(subset_to_singletons).T.plot(y='z_t', marker='.', label='profile')

plt.axvline(ds.TEMP.isel(subset_to_singletons).isel(z_t=0), 
            linewidth=0.5, c='tab:red', label='surface')

plt.axvline(ds.TEMP.isel(subset_to_singletons).isel(z_t=0)+dsigma, 
            linewidth=0.5, c='tab:blue', label='S at mld')

plt.axhline(temp_depth*1e2, linewidth=1., c='k', label='MLD')

plt.legend(loc=(1.02, 0));
ylm = plt.ylim()
plt.ylim(ylm[::-1]);
```
![MLD example plot](images/mld_example_plot.png)

## Running this on the Entire Dataset
Now let's put everything together, running the `mld_dsigma` calculation on the "full" dataset (note that it is still subset given the smaller domain mentioned previously).

```python
%%time
mld = mld_dsigma(ds.SALT, ds.TEMP).compute()
```