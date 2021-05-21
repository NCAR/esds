---
author: Max Grover
date: 2021-5-21
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
- Minimum reproducible examples don't always work - instead, curate domain-specific examples
- STAC (spatio-temporal asset catalog) can be helpful when working with satellite imagery, making it easy to search for specific datasets
  - Similar to intake, able to search spatially as well

## [Growth and History of Anaconda + Numpy + SciPy + Dask](https://zoom.us/rec/share/_KQiagnZBnW0xPIHAHZZs553JuFsJXfkQpdwUmTca7-QE91safAQCefSYr6-Kz3R.EDHHYf_864Dw3v8Q?startTime=1621515755000)

This session was a keynote focused on how these packages + ecosystem grew

- Key question - how do you get from a few passionate few to productive many?
  - Keep your motivated few to less than 5 people
- Where efforts should be focused
  - Dedicating full time employees to work on community dev projects
  - Build the community as you go - this is essential
    - Sometimes it takes a while to build up your product... that's okay!
- Working code solves most arguements
  - At the end of the day, someone has to sit down and code something up.. if it works, great!
- Great projects start with a need
  - The conceptual idea is not always important - specific use cases are more important
- You need to solve **_something_**
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
- **_Provide scope and build people_**
  - Move towards "grassroots" not so much top down

## How can we tie this back to ESDS?

Several of these sessions included speakers/organizers from within NCAR, such as Anderson Banihirwe [(@andersy005)](https://github.com/andersy005) and Deepak Cherian [(@dcherian)](https://github.com/dcherian). They, along with several others with NCAR, could be considered the "passionate few". They are core developers of upstream projects such as Xarray and Dask, which are critical components to the scientific python ecosystem, especially for geoscience. The key to ESDS is growing the userbase, moving toward the "productive many".

We should see the ESDS initiative as an opportunity to test out these ideas, and push to forge ahead with a grassroots movement focused around promoting open-science and open-devlopment, empowering people to be more productive in their data workflows. Here are a few key points for us to consider:

- Developing in small teams
- Continue to use Dask for scalable analysis using our HPC resources
- Stressing the importance of open-science, providing examples of what this looks like
- Documenting complex scientific workflows
- Continue to explore moving toward cloud-native datasets
- Focus efforts on training people, making them contributors

We should continue to foster collaboration across NCAR, finding opportunities to share our workflows, find improved methods of sharing code, and move outside of our typical "silos", toward a more open, inclusive, and collaborative environment. We can build on the tools already available within the scientific Python ecosystem, such as Dask, to continue to gather insight from the daily "big data"
