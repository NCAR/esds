## Using Dask on the New Casper PBS Scheduler

Starting soon, the NCAR Jupyterhub [https://jupyterhub.ucar.edu] will be updated and require users to utilize PBS instead of SLURM. This impacts the way Dask is spun up within notebooks... below is an example a configuration suitable for the new setup!

### Example using new Casper-batch login

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
    resource_spec='select=1:ncpus=24:mem=100GB', # Specify resources
    project='project_id', # Input your project ID here
    walltime='02:00:00', # Amount of wall time
    interface='ib0', # Interface to use
)

# Scale up
cluster.scale(10)

# Setup your client
client = Client(cluster)

# Change your url to the dask dashboard so you can see it
dask.config.set({'distributed.dashboard.link':'https://jupyterhub.hpc.ucar.edu/stable/user/{USER}/proxy/{port}/status'})
```
Now, if you run just `client`, it should return information about your client and cluster, including the dashboard.

Now onto computing!
