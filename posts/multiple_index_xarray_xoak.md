---
author: Max Grover
date: 2021-4-23
tags: xarray, xoak, index
---

# Dealing with Multi-Indexing Coordinates and the Power of Xoak

This week, there a post within the Zulip regarding how to deal with indexing [CAM-SE](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2017MS001257) data. The tricky part here is that is an unstructured grid, where there is only one column to the data, `ncol`.

Using the [Multiple-level indexing documentation](http://xarray.pydata.org/en/stable/indexing.html#multi-level-indexing) within Xarray didn't seem to help... so what other options are there?

This is a situation where using [Xoak](https://xoak.readthedocs.io/en/latest/) comes in handy. Xoak is an xarray extension, or add-on, which makes dealing with these irregular dimensions easier. It utilizes [SciPy's cKDTree adaptor](https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.cKDTree.html).

There a few greate examples on their documentation including:

- [High-level introduction](https://xoak.readthedocs.io/en/latest/examples/introduction.html)
- [Dealing with larger data](https://xoak.readthedocs.io/en/latest/examples/dask_support.html)

For **_this_** specific issue though, we can use Xoak to deal with these latitudes and longitudes which have the same dimension, `ncol`.

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
