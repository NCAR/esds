---
author: Max Grover
date: 2021-4-23
tags: xarray, xoak, index
---

# Indexing unstructured grids with the Power of Xoak

This week, there a post within the Zulip regarding how to deal with indexing [CAM-SE](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2017MS001257) data. The tricky part here is that is an unstructured grid, where there is only one column to the data, `ncol`.

Here is an example of the dataset we are working with. Notice that both lat and lon have the same dimension, `ncol`.

```
<xarray.Dataset>
Dimensions:    (nbnd: 2, ncol: 777602, time: 5772)
Coordinates:
  * time       (time) object 0021-02-01 00:00:00 ... 0502-01-01 00:00:00
Dimensions without coordinates: nbnd, ncol
Data variables:
    lat        (ncol) float64 ...
    area       (ncol) float64 ...
    lon        (ncol) float64 ...
    time_bnds  (time, nbnd) object 0021-01-01 00:00:00 ... 0502-01-01 00:00:00
    PSL        (time, ncol) float32 ...
Attributes: (12/13)
    np:               4
    ne:               120
    Conventions:      CF-1.0
    source:           CAM
    case:             B.E.13.B1850C5.ne120_t12.sehires38.003.sunway_02
    title:            UNSET
    ...               ...
    host:             psn012
    Version:          $Name$
    revision_Id:      $Id$
    initial_file:     B.E.13.B1850C5.ne120_t12.sehires38.003.cam.i.0021-01-01...
    topography_file:  /home/export/online1/xwan/cesm/inputdata/atm/cam/topo/U...
    NCO:              netCDF Operators version 4.7.9 (Homepage = http://nco.s...

```

Using the [Multiple-level indexing documentation](http://xarray.pydata.org/en/stable/indexing.html#multi-level-indexing) within Xarray didn't seem to help... so what other options are there?

This is a situation where using [Xoak](https://xoak.readthedocs.io/en/latest/) comes in handy. Xoak is an xarray extension, or add-on, which makes dealing with these irregular dimensions easier. It utilizes [SciPy's cKDTree adaptor](https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.cKDTree.html).

There a few great examples on their documentation including:

- [High-level introduction](https://xoak.readthedocs.io/en/latest/examples/introduction.html)
- [Dealing with larger data](https://xoak.readthedocs.io/en/latest/examples/dask_support.html)

For **_this_** specific issue though, we can use Xoak to deal with these latitudes and longitudes which have the same dimension, `ncol`.

Before using xoak for selecting data, there is one modification we need to make to the dataset. In the output from xarray, notice how `lat` and `lon` are not included in the coordinates. Xoak expects `latitude` and `longitude` to be coordinates, so we make a slight modification, setting these two variables to be coordinates.

```python
ds = ds.set_coords(['lat', 'lon'])
```

Now that we have our dataset ready for xoak, we can setup our function and apply it for the lats/lons we are interested in looking at.

```python
import xoak

# Setup a function to deal with flexible indexing
def kdtree_sel(ds, lats, lons):
    """
    Uses xoak to select data with irregular dimensions

    Parameters
    ----------
    ds : `xarray.Dataset`
      Dataset with your data, with lat/lon dims in one-dimension

    lats : list
      List of latitudes to select

    lons : list
      List of longitudes to select

    Returns
    -------
    ds : `xr.Dataset`
      Dataset subset based on input lats/lons
    """

    # Checks to see if this has an xoak index - if not, create one using the extension
    if not ds.xoak.index:
        ds.xoak.set_index(("lat", "lon"), "scipy_kdtree")

    # Return the selected datasets
    return ds.xoak.sel(lat=xr.Variable("ncol", lats), lon=xr.Variable("ncol", lons))


kdtree_sel(ds, [34, 34.25, 34.3, 42], [350, 350, 352, 290])
```

Where the resultant time to compute and resultant dataset are given below. Notice the performance of this indexing method (`283 ms`).

```
CPU times: user 244 ms, sys: 13.8 ms, total: 258 ms
Wall time: 283 ms
<xarray.Dataset>
Dimensions:    (nbnd: 2, ncol: 4, time: 5772)
Coordinates:
  * time       (time) object 0021-02-01 00:00:00 ... 0502-01-01 00:00:00
    lat        (ncol) float64 34.1 34.3 34.24 41.92
    lon        (ncol) float64 350.0 350.0 352.0 290.0
Dimensions without coordinates: nbnd, ncol
Data variables:
    area       (ncol) float64 ...
    time_bnds  (time, nbnd) object ...
    PSL        (time, ncol) float32 ...
Attributes: (12/13)
    np:               4
    ne:               120
    Conventions:      CF-1.0
    source:           CAM
    case:             B.E.13.B1850C5.ne120_t12.sehires38.003.sunway_02
    title:            UNSET
    ...               ...
    host:             psn012
    Version:          $Name$
    revision_Id:      $Id$
    initial_file:     B.E.13.B1850C5.ne120_t12.sehires38.003.cam.i.0021-01-01...
    topography_file:  /home/export/online1/xwan/cesm/inputdata/atm/cam/topo/U...
    NCO:              netCDF Operators version 4.7.9 (Homepage = http://nco.s...
```
