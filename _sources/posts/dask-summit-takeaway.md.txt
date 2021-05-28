---
author: Max Grover
date: 2021-5-28
tags: dask, conference, open-science
---

# Dask Distributed Summit 2021 Takeaways

## [Pangeo Session](https://zoom.us/rec/play/bVuz_sZOnzsH8fJdrsvH7T_XgXBg64cRSgbV4PERZByVgoLzUDXXoc1pq02Hcfg1oxE7uzAa919Jly1p.tmy6yMikcfgRVHi2?startTime=1621447260000&_x_zm_rtaid=P6Q_HcGvQa-lvvjzHzq4Rg.1621536889692.ea182bc019aed9fbea835c35b62d5ca5&_x_zm_rhtaid=831)

- Cloud optimized datasets help improve speed of analysis
  - Entire 4 TB datasets open up in a few seconds
  - Important to chunk you data - store in object-store
- Reading netcdf data remotely, especially on the cloud, can take a while...
  - Even with using dask-delayed, quite slow
- Open-source projects, such as XGCM, make answering big science questions easier
  - Ex. looking at oxygen minimum zones, converting to density coords
- Persistent pain points
  - Using dask vs. understanding dask - can we make this transition easier for non-daskers?
  - It can tough to pin down specific parts of code which is causing workers to die
- We should get more science workflows in the cloud
  - Ensure these workflows are documented, especially in relation to dask
  - Document cases of Dask workers being killed and how to go about solving these issues
    - "Dask worker serial killers"
- Minimum reproducible examples don't always work - instead, curate domain-specific examples
- STAC (spatio-temporal asset catalog) can be helpful when working with satellite imagery, making it easy to search for specific datasets
  - Similar to intake, able to search spatially as well
  - Recent development of [StackStac](https://stackstac.readthedocs.io/en/latest/) allows for fast loading of STAC catalogs

### [Pangeo Session Talk Links](https://summit.dask.org/schedule/presentation/1/pangeo/)

- Chelle: notebook can be found in folder AWS-notebooks
  - [Jupyter Notebooks](https://github.com/pangeo-gallery/osm2020tutorial)
- Julius:
  - [Slides](https://speakerdeck.com/jbusecke/dask-and-the-ocean-death-zones-lessons-from-a-real-life-earth-science-workflow-with-a-fullish-pangeo-stack)
  - [CMIP6 Prepocessing](https://github.com/jbusecke/cmip6_preprocessing)
  - [Oxygen Minimum Zones Paper Preprint](https://www.essoar.org/doi/10.1002/essoar.10507050.1)
- Rob
  - [Info about STAC specification](https://stacspec.org)
- Deepak:
  - [Dask Groupby Repository](https://github.com/dcherian/dask_groupby)
- Haiying:
  - [Pangeo Benchmarking Repository](https://github.com/pangeo-data/benchmarking)
- Damien:
  - [Software Carpentries Lessons](https://github.com/carpentrieslab/python-aos-lesson)

## [Growth and History of Anaconda + Numpy + SciPy + Dask](https://zoom.us/rec/share/_KQiagnZBnW0xPIHAHZZs553JuFsJXfkQpdwUmTca7-QE91safAQCefSYr6-Kz3R.EDHHYf_864Dw3v8Q?startTime=1621515755000)

This session was a keynote focused on how these packages + ecosystem grew

- Key question - how do you get from a few passionate few to productive many?
  - Keep your motivated few to less than 5 people
- Where efforts should be focused
  - Dedicating full time employees to work on community dev projects
  - Build the community as you go - this is essential
    - Sometimes it takes a while to build up your product... that's okay!
- Really successful projects limit scope and provide interfaces
  - Maybe success means that a project becomes an interface and becomes an underlying layer for something else
- Working code solves most arguements
  - At the end of the day, someone has to sit down and code something up.. if it works, great!
- Great projects start with a need
  - The conceptual idea is not always important - specific use cases are more important
- Start by solving **_something_**
  - This may require shrinking the scope to a more manageable size
- Let teams go and do their own thing
  - Taken scope -> give to others -> do that thing
- You need to be humble with your project, but not too humble; simple but not too simple
  - It is all about balance
- Top down approaches typically do not work
  - You will always want more resources...
- The power of Python is the community
  - Key idea - **_there are more smart people outside of your organization than inside your organization_**
  - If you try to do everything, it will inevitably fail - need to make it more simple
  - Unlock the community - entrain users, become contributors
- At some point, it transitions to where you ["give away your legos"](https://review.firstround.com/give-away-your-legos-and-other-commandments-for-scaling-startups)
- **_Provide scope and build people_**
  - Move towards "grassroots" not so much top down

## [Xarray User Forum + Updates](https://zoom.us/rec/share/3AnbFtOiRIARD3A6MdM1F0PrMvpASQxJQNWbt6pppYpRrx33EFGQYy-wLQWVQZ-H.bl2gwN915ju9aidF?startTime=1621402478000)

- Xarray now includes a backend api, allowing contributors to add new backends for reading + operating on datasets
  - Including the `raw_indexing` method is important to enable lazy loading
- Flexible indexing is coming to xarray soon
  - Helps when dealing with irregular spaced data, working with projected coordinate systems, staggered grids (ex. 2D lat-lon coordinate variables)
  - Currently, Xarray uses pandas for indexing, which is problematic when wanting to do flexible indexing, only supporting 1D in-memory indexes
  - Current Xarray accessor - [Xoak](https://xoak.readthedocs.io/en/latest/)
    - See [previous blog post on working with unstructured grids](https://ncar.github.io/esds/posts/multiple_index_xarray_xoak/)
  - See the [design documents for flexible indexing in Xarray](https://github.com/pydata/xarray/blob/master/design_notes/flexible_indexes_notes.md)
- Duck arrays are now supported in Xarray
  - Duck arrays are arrays that **_look_** like numpy arrays in the sense that they have a similar api, but are fundamentally different data types (Ex. a [pint](https://pint.readthedocs.io/en/stable/tutorial.html) array which looks like a numpy array)
  - Helps when working with [pint](https://pint.readthedocs.io/en/stable/)
  - Other examples of duck arrays
    - [SciPy Sparse Matrices](https://docs.scipy.org/doc/scipy/reference/sparse.html)
    - [CuPy](https://docs.cupy.dev/en/stable/user_guide/basic.html)
  - **_Most_** of the xarray API supports duck arrays, few aspects that still don't

### [Xarray User Forum Talk Links](https://summit.dask.org/schedule/presentation/51/xarray-user-forum/)

- Aureliana Barghini’s Talk

  - [New backend plugin infrastructure](https://github.com/aurghs/xarray-backend-tutorial)

- Links from Benoit Bovy’s talk

  - [Flexible indexes design notes](https://github.com/pydata/xarray/blob/master/design_notes/flexible_indexes_notes.md)
  - [Explicit indexes project](https://github.com/pydata/xarray/projects/1)

- Davis Bennett’s talk

  - [Hierarchical storage data structure in xarray](https://github.com/pydata/xarray/issues/4118)

- Ravi Kumar’s talk:
  - [Using Xarray to store statistical diagnostic data](https://github.com/arviz-devs/arviz_misc/tree/master/xarray_user_forum_2021)

## [Dask on High Performance Computing Systems](https://zoom.us/rec/share/25oqsPdh_ZeZSFmvvbOLzJ0Sa8Q7py6GiLrVra8UHJmi0rZ1YLm69Jpt9NUiN4Cm.1MS7-WLlIPa3Ewku?startTime=1621519269000)

- Dask-jobqueue provides a uniform api to spinning up dask-clusters, interfacing with scheduler
- MPI-based communication with Dask shows promising results
- We are fortunate to have the HPC system we have (Cheyenne/Casper)
  - In terms of data access, integration of compute and login nodes
  - [NCAR JupyterHub](jupyterhub.ucar.edu) which enables improved access to Jupyter environment

### [Dask on HPC Talk Links](https://summit.dask.org/schedule/presentation/34/dask-in-hpc/)

- Anderson
  - The Current State of Deploying Dask on HPC Systems
    - [Presentation](https://talks.andersonbanihirwe.dev/deploying-dask-on-hpc-dask-summit-2021.html)
    - [Notebook example](https://nbviewer.jupyter.org/github/andersy005/brouillons-quotidien/blob/main/dask/dask-cupy-multi-node-gpu.ipynb)
- Tina
  - Real Time Monitoring of HPC Simulation Outputs using Dask and Xarray
    - [Dask scheduler written in Rust](https://github.com/It4innovations/rsds)

## How can we tie this back to ESDS?

Several of these sessions included speakers/organizers from within NCAR, such as Anderson Banihirwe [(@andersy005)](https://github.com/andersy005) and Deepak Cherian [(@dcherian)](https://github.com/dcherian). They, along with several others with NCAR, could be considered the "passionate few". They are core developers of upstream projects such as Xarray and Dask, which are critical components to the scientific python ecosystem, especially for geoscience. The key to ESDS is growing the userbase, moving toward the "productive many".

We should see the ESDS initiative as an opportunity to test out these ideas, and push to forge ahead with a grassroots movement focused around promoting open-science and open-devlopment, empowering people to be more productive in their data workflows. Here are a few key points for us to consider:

- Developing in small teams
- Continue to use Dask for scalable analysis using our HPC resources
- Stressing the importance of open-science, providing examples of what this looks like
- Documenting complex scientific workflows
- Continue to explore moving toward cloud-native datasets
- Focus efforts on training people, making them contributors

We should continue to foster collaboration across NCAR, finding opportunities to share our workflows, find improved methods of sharing code, and move outside of our typical "silos", toward a more open, inclusive, and collaborative environment. We can build on the tools already available within the scientific Python ecosystem, such as Dask, to continue to gather insight from large datasets within the geoscience community.
