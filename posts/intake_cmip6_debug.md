---
author: Max Grover
date: 2021-5-14
tags: intake, cmip6, debug
---

# Debugging Intake-ESM Process for Reading in CMIP6

This post was motivated by a post from Steve Yeager [@sgyeager](https://github.com/sgyeager), who ran into an error when attempting to read in CMIP6 data via intake-esm.

For those who are unfamiliar with intake-esm, be sure to read over [the documentation](https://intake-esm.readthedocs.io/en/latest/index.html)! The user guide even includes [an entire portion of their site](https://intake-esm.readthedocs.io/en/latest/user-guide/cmip6-tutorial.html) on looking at CMIP6 data. These resources would be a great place to start.

The specific workflow of using this package for reading in Sea Water Silinity (`so`) and
Sea Water Potential Temperature (`thetao`) are given below

## Reproducing the Error

```python
import intake
```

Set a path to the CMIP catalog - in this case, since we using the glade file system, use this and open the catalog using the intake-esm extension.

```python
# Set the path for the catalog file
catalog_file = '/glade/collections/cmip/catalog/intake-esm-datastore/catalogs/glade-cmip6.json'

# Open the catalog using intake
col = intake.open_esm_datastore(catalog_file)
```

Now, we set which experiment to use. In this case, we are interested in the Ocean Model Intercomparison Project (OMIP) since we are looking at ocean data, setting

```python
experiment_id = ['omip1']
```

In terms of the variables of interest, we are interested in Sea Water Silinity (`so`) and Sea Water Potential Temperature (`thetao`), so we set

```python
variable_id = ['so', 'thetao']
```

The last variable to change is the table_id which corresponds to the temporal frequency. Since we are interested in monthly data, we set

```python
table_id = 'Omon'
```

Putting all that together, we setup the catalog and call `to_dataset_dict` which assembles a dictionary of datasets

```python
cat = col.search(
    experiment_id=['omip1'],
    variable_id=['thetao', 'so'],
    table_id='Omon'
)
dset_dict = cat.to_dataset_dict()
```

But this returns an error of:

```
AggregationError:
        Failed to merge multiple datasets in group with key=OMIP.CNRM-CERFACS.CNRM-CM6-1.omip1.Omon.gn into a single xarray Dataset as variables.

        *** Arguments passed to xarray.merge() ***:

        - objs: a list of 2 datasets
        - kwargs: {}

        ********************************************
```

## Determining the Cause of the Error

At this point, let's go back and inspect the subset catalog we have, calling the `catalog.df`

```python
cat.df
```

Notice how in the error, the source_id which triggered the error is `CNRM-CM6-1`, so let's subset for that and investigate the problem...

```python
cat.df[cat.df.source_id == 'CNRM-CM6-1']
```

Here, we focus on the `time_range` column - noticing that the last time step for `so` is `194912` while the last timestep for datasets with `thetao` is `199912`, with the dates formatted `YYYYMM`.

When intake attempts to concatentate these two datasets, with different times, it struggles and returns the error that it cannot merge them together since the length of the time axis differs.

## Applying our Solution

To fix this problem, If you would like to still work with the data, you will need to read in datasets using separate queries as shown below

```python
# Search and read in dataset for so
cat_so = col.search(
    experiment_id=['omip1'],
    variable_id=['so'],
    table_id='Omon'
)
dset_dict_so = cat_so.to_dataset_dict()

# Search and read in dataset for thetao
cat_thetao = col.search(
    experiment_id=['omip1'],
    variable_id=['thetao'],
    table_id='Omon'
)
dset_dict_thetao = cat_thetao.to_dataset_dict()
```

Another option would have been to specify within .to_dataset_dict() to not aggregate the datasets, using the following syntax .to_dataset_dict(aggregate=False), but it can be difficult using this functionality with such a large number of ensemble members.

I hope this helps with your intake-esm usage! Happy computing!
