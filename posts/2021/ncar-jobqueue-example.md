---
author: Max Grover
date: 2021-4-15
tags: jupyterhub, dask, ncar
---

# NCAR-Jobqueue

Last week, we added posts detailing how to configure [Dask](https://docs.dask.org/en/latest/) using the new PBS scheduler on [Casper](https://www2.cisl.ucar.edu/resources/computational-systems/casper). In this week's example, we provide an example of the recent updates to [ncar-jobqueue](https://github.com/NCAR/ncar-jobqueue), added by [Anderson Banihirwe](https://github.com/andersy005), which allow users to easily configure dask on Casper without having to add many extra steps.

## How can I use the new updates to NCAR-jobqueue?

You must update the package to use the newest updates. You can update using conda!

```python
conda update ncar-jobqueue
```

If you haven't installed this package yet, replace the previous line with

```python
conda install -c conda-forge ncar-jobqueue
```

## How is NCAR-Jobqueue different than Dask-Jobqueue

NCAR-jobqueue was created to easily interface Dask-Jobqueue, with the focus on using NCAR machines such as Casper or Cheyenne. NCAR-jobqueue sets up your PBS Cluster, using the same arguements as you would enter in the more general Dask-Jobqueue.

## How would I use this on within my workflow on Casper?

The overall workflow is the same - you inport dask related packages, configure your cluster, the scale your job depending on the number of jobs you would like. In last week's example, we used the following example:

```python
cluster = PBSCluster(
    cores=1, # The number of cores you want
    memory='10GB', # Amount of memory
    processes=1, # How many processes
    queue='casper', # The type of queue to utilize (/glade/u/apps/dav/opt/usr/bin/execcasper)
    local_directory='$TMPDIR', # Use your local directory
    resource_spec='select=1:ncpus=1:mem=10GB', # Specify resources
    project='project_id', # Input your project ID here
    walltime='02:00:00', # Amount of wall time
    interface='ib0', # Interface to use
)
```

Where once you update `~/.config/dask/jobqueue.yaml` file with your desired parameters, you can use

`cluster = PBSCluster(queue='casper')`

Although, you would still need to port the Dask dashboard using this line

```python
# Change your url to the dask dashboard so you can see it
dask.config.set({'distributed.dashboard.link':'https://jupyterhub.hpc.ucar.edu/stable/user/{USER}/proxy/{port}/status'})
```

Instead, using ncar-jobqueue, we use the following:

```python
from ncar_jobqueue import NCARCluster
from dask.distributed import Client
cluster = NCARCluster(project='XXXXXXXX')
cluster.scale(jobs=2)
client = Client(cluster)
```

This sets up the scheduler, spins up the cluster, and edits Dask dashboard url so you can easily click it to view it. You are still able to configure arguements within `NCARCluster` as you would in `PBSCluster`, but ncar-jobqueue handles many of the system-specific defaults for you.

While this example covers how to use it on Casper, this same ncar-jobqueue example could be used on Cheyenne, without having to change anything!

Shoutout to Anderson for updating this package and making using Dask on Casper/Cheyenne much easier!
