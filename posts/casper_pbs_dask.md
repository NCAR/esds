---
author: Max Grover
date: 2021-4-06
tags: jupyterhub, dask
---

# Using Dask on the New Casper PBS Scheduler

Casper will complete a transition from Slurm to the PBS Pro workload manager on April 7, 2021. This has implications for how to spin up a Dask cluster, including via the [NCAR Jupyterhub](https://jupyterhub.ucar.edu).

Below is an example script suitable for the new configuration using the `PBSCluster` function from `dask_jobqueue`. Note that the `ncar_jobqueue` package [requires updating](https://github.com/NCAR/ncar-jobqueue/issues/40) to work with the new configuration.

## Example using new Casper-batch login

```python
# Import dask
import dask

# Use dask jobqueue
from dask_jobqueue import PBSCluster

# Import a client
from dask.distributed import Client

# Setup your PBSCluster
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

# Scale up
cluster.scale(2)

# Change your url to the dask dashboard so you can see it
dask.config.set({'distributed.dashboard.link':'https://jupyterhub.hpc.ucar.edu/stable/user/{USER}/proxy/{port}/status'})

# Setup your client
client = Client(cluster)

```

Now, if you run just `client`, it should return information about your client and cluster, including the dashboard.

There are a few parts of the `PBSCluster` object which are stored in `~/.config/dask/jobqueue.yaml`, so you can shorten the cluster portion of the script to something like

```python
# Setup your PBSCluster - make sure that it uses the casper queue
cluster = PBSCluster(queue='casper')
```

Now onto computing!
