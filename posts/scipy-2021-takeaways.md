---
author: Max Grover
date: 2021-7-16
tags: conference, scipy, open-source
---

# SciPy Conference 2021 Takeaways

This week, I had an opportunity to (virtually) attend the Scientific Computing with Python (SciPy) Conference! The conference consisted of three primary sections:

- Tutorials (Monday/Tuesday)
- Talks (Wednesday - Friday)
- Sprints (Friday - Sunday)

Tutorial topics ranged from machine learning, interactive dashboards, to distributed computing using Dask! These tutorials were four hours long, including a wide variety of speakers for each tutorial topic.

The talks included keynote addresses at the beginning of the day, followed by various tracks, typically including some "scientific-focused" session (ex. "Earth, Ocean, Geo, and Atmospheric Science"), a machine learning track, and maintainer track. The variety of tracks offer an opportunity to group into more focused disciplines/groups. Personally, my favorite session was the Earth, Ocean, Geo and Atmospheric Science session, which was held Friday morning through afternoon (Central time)

## Keynote - Fernando Perez - SciPy and Open Source Toolsin Sicence: Challenges and Successes

### Background

- iPython - an afernoon hack in October 2001
  - Collaborative effort from the beginning
  - Announced iPython in 2001
- Other things in 2001
  - Enthought
  - iPython
- wouldn't be here without this community
- So far - mostly white men - need to move toward more diversity in the field
  - Grant to push for more diversity - led by group at CU Boulder
- It takes a village
  - Large variety of packages + tools
  - 2015 - black holes - first figure was plotted in Python
  - 2019 - first image of black hole - cited numpy and scipy
    - 23,000 people contributed to the code behind this
- 10 most influential code bases
  - IPython/Jupyter - really a lot of the packages that go into this
- Students at UC Berkely
  - Most students using Jupyter, organize a national data science workshop now

## Open dev model

- Too much ad-hoc volunteer work - only those who volunteer can participate
- Structural funding?
  - Maintenance
  - Documentation
  - Community dev
  - Strategic planning
  - Cross-project coordination
- Academic careers?
  - Postdocs, students, RSEs, faculty
- Industry ("big tech"?)
- **Software is more than papers and code**
  - Services and content - impact
  - Software
  - Standards and Protocols - ecosystem
  - Community - innovation and resiliency
- Jupyter - language agnostic!
  - Document ideas - later support other languages(R, Julia, etc.)
    - Over 100 kernels!
- Governance - managed and govern sustainability
- How do we do this for another 20 years?
  - Limited direct federal $$$
  - Indirectly
    - Lots of $ have supported Scientific OSS
  - Who stepped in?
    - Private philanthropy
    - Alfred P. Sloan, Gordon and Betty Moore, Chan Zuckerberg
- Catastrophic success: an economic problem
  - Python has overtaken IDL
  - Today, Python by a wide margin, is the most popular interpreted language in astronomy
  - Mathworks - 4000 employees
  - Wolfram - 800 employees
  - IDL/Harris - 17,000 employees
  - We need to think about this as a risk of science
- Scientific OSS is a foundational public good
  - Roads and Bridges - the Unseen labor behind our digital infrastructure - needs maintenance and support
  - Can't just give some PI money to build it - need long term support
- Resources
  - Federal research and dev budget - $200 million per year
    - What fraction of R&D depends on computing?
  - $2 Billion is 1% - would make a HUGE difference
- Some features of successful, resilient projects
  - Broad community engagement
  - Actively managed pipeline for new contributions
  - Capacity for short and long term funding
- Funded full-time backbone teams
  - Maintenance, documentation, tech deep dives
  - Strategic planning, fundraising, operations, community dev
- Professionalization is inclusive
  - Reliance on volunteers excludes people!
- Efforts with larger orgs
  - NumFocus
- JOSS - Journal of Open Source Software
  - Established academic publishers - see this as a threat
  - Cheaper and better - rethinking these models
- Career paths
  - Society of research engineering - Europe
  - US Research Software Engineer Association
    - Create sustainable paths for this
- Mozilla
  - Leading professional dev opportunities, in leadership for open source
- 2i2c
  - Non-profit that takes some of work with infrastructure, scale computing for science
  - Doing these in academia - lots of infrastructure to do
  - 2i2c - manage the infrastructure and support open source
    - Sustaining the ecosystem
- Jupyter Community Workshops
  - Good opportunity to explore some of these questions
  - Conversations about sustainability - federal partnerships
- Now have enough for success, but have a much larger need now
  - Other agencies thinking about this - get resources on foundational side

## [Atmospheric data Community Toolkit](https://github.com/ARM-DOE/ACT)

- Framing the problem
  - Didn't really have CS incoporated into curriculum
    - Learned java + c, not for data analysis...
  - Advisors just dump their code
    - Their way becomes your way!
    - Can be tough to build up from there...
  - Get into job market - different groups do things differently
  - Build up coding silos - makes it difficult to share across groups
    - Even in same organizations!
    - Silos are built on 20 years of doing things...
  - If you have flexibility, can build from there
    - Adjust and break out of the coding silos
  - When you can contribute across organizations, get more people on board
    - Contribute to the greater community
- Atmospheric Science side
  - See a gap for toolkit for atmospheric observations
  - Toolkit for data exploration and analysis of atmospheric time-series datasets
  - Pulling from xarray, pandas, MetPy
- Atmospheric data Community Toolkit
  - Data exploration, analysis of time-series data
  - IO
  - Deploy instrumentation around the world
  - Want to share the code base across all of these
  - Read in, visualize
  - Goals
    - Bridge research communities
    - Reduce duplication of effort
    - Transparency
    - Flexibility

### Discovery

- ARM Live Data Web Service
  - PB of data back to 1993
- ASOS
  - API from iowa mesonet
- USDS Cropscape
  - Croptype is very important!
- IO
  - xarray for netcdf
  - Pandas for text/csv files
  - Specific readers for NOAA global monitoring network
    - Surface met, radiation
  - Binary micropulse lidar using MPL2NC
    - Create temporary netcdf file
  - Cole data file structures from ARM program to create "empty" datasets - fill with missing values
- Corrections
  - Correct lidar data like micropulse lidar for deadtime, afterpulse
  - Correcting ceilometer data for easier visual analysis
  - Wind-corrections for ship motion
- Able to add contributors to zenodo - get people credit!
- Retrievals
  - Wind profiles from Scanning Doppler Lidar
    - PyART can be used for lidar too!
  - Sky infrared temperature fro AERI irradiances
  - Solar radiation calculations
    - Net radiation, longwave radiance
  - Sea surface temperature from infrared radiometer measurments
- Quality control
  - Apply additional tests
    - Simple limit tests
  - Using bit-packed QC to allow for multiple tests
  - Plotting tools to visualize - example - simple limit test
- More
  - Prioritized visualization at first
    - Timeseries plots
    - Vertical profiles
    - MetPy - soundings
    - Generate combined plots as needed
    - Use pyART for other aspects
  - General utils
    - Precip accumulation
    - Weighted averaging
- Future dev
  - Boundary layer height calc
  - Interactive plotting
  - 3D viz
- How do you coordinate with the model diagnostics community?
  - Earth Model Column Collaboratory
  - https://github.com/columncolab/EMC2
  - [Example notebook](https://nbviewer.jupyter.org/github/columncolab/EMC2/blob/master/doc/source/EMC2example.ipynb)
- Moving toward open development
  - Needed to convince program managers
  - Convince that the wider community is using, addint to it
  - Worked with ARM group to get this going

## [OCEtrac - Ocetrac: morphological image processing for monitoring marine heatwaves](https://github.com/ocetrac/scipy2021-talk)

- See warming trend in the oceans...
  - Lots of variability on top of this
  - Compute trend at every point you have data for
  - Can cause marine heatwaves to form
- Species can cope with fluctuations in temperature
  - If we continue to warm the climate, warm extremes more frequent, more extreme
- Marine events exceed some threshold over some 30 year time period
  - Can be broader across ocean, or more locally focused
- Motivation
  - Marine heatwaves don't stay in one place
  - Complex spatial connectivity and temporal behavior
  - Local analyses may be completely characterize evolution
  - Can we build a tool to identify and track these?
- Goals of OceTRAC
  - ID marine heatwaves as 2D object from SST anomalies
  - Track marine heatwave objects in space and time
  - Create new labeled dataset of heatwaves
- NOAA Optimum Interpolation SST (OISST)
  - Mean SSTs - bias corrected
  - Compute SST anomalies
  - Extract only 90th percentile of SST anoms
  - NOAA OISST data - on s3 object storage
    - use pangeo forge to convert from netcdf to zarr
- running notebook
  - get your dask cluster
  - Do some preprocessing
    - Need to do this before feeding in
  - Convert into a binary map - if exceed, label 1 - if not, 0
    - Can do this for any type of phenomena
    - Can use this for any feature id
  - After you have this, use SciPy.ndimage
    - Open/close - smooth contours of image
      - Close - fill small holes in features
      - open - eliminate small features
  - Structuring element
    - Radius - define size of element (what is used to construct object)
  - Once you have object, collect the area (objects below threshold removed)
  - Last part - track in space and time
    - Connectivity element - connected in x, y, time
      - If they are connected, share the same id
    - These can merge, come together, split
      - Heat wave remembers the history

### Running this

- Load in data array
- Set radius to number of grid points
- Minimum size quartile - threshold for object areas
- xdim, ydim
- Tracker object

  - Feed in data array, mask, radius, min*size*

- Each color on there is a different heavwave
  - Can see size and shape of these
  - Can zoom into single events
- Can look at more stats using regional properties
- Now have quantified dataset to understand the event

### New Insights

- Seen two different patterns evolve - regional, global
  - Tropics play big role in global scale
- Global heat waves last longer, more intense
- Marine heatwaves split and merge, connected in space and time
- Can track any ocean variables you want
- Dealing with the 180 degree seam
  - Something they had to add on...
