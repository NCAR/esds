---
author: Max Grover
date: 2021-3-26
tags: townhall, cgd, questions
---

# NCAR-CGD ESDS Town Hall

Last week, there was a town hall focused on gathering input on the Earth System Data Science initiative at NCAR. The meeting began with an introduction about the initiative, the vision, goals, and how the team is planning to start working toward these goals.

The Question/Answer portion of the town hall was very informative and brought up some great topics for discussion. They have been collected from both the chat and Google Doc, sorted by category.

While there are tentative “answers” under each question, these are by no means absolute answers - but rather a starting point to answer these questions. We look forward to further collaboration and development of this initiative.

## Question and Answer Portion

### Asking Questions

Can there be technology-mentors which can help answer questions outside of the WIP meetings?

- One-on-one interaction is great, but doesn’t scale - in order to address this, we suggest having “code-clinics” where people interested in assistance can pair with a mentor. In addition to this, people can ask for help in various channels on Zulip, where questions can be “binned” into FAQs, which become blog posts (ex. How to use Dask on Cheyenne/Casper)
- The focus will be on providing both spaces for people to ask one-on-one questions, and providing better documentation through examples/blog posts

### Dask

How do we promote best practices with Dask?

- Build community resources for Dask
- Offer a simple, containerized tutorial and apply this to a real workflow
- Cover best practices, how to scale, etc.
- Offer in conjunction with XDev
- Collaborate with GeoCAT team, Project Pythia for training and examples

### Publications and Citations

For packages specific to publications, how do they work into the ecosystem?

- Publication specific publications build on the ecosystem, can be archived through Zenodo or through working with the NCAR library to add a DOI

### How do we find these projects?

Come up with list of projects associated with a dataset and or repository (helping to prevent from reinventing the wheel)

- _Potential collaboration with RDA?_

### Funding

Many CGD people are on soft money and using the easiest and fastest method is typically preferred, but if you want something more broadly usable with best practices and documentation, that takes longer and requires more resources. How do we address this issue?

- Leverage the expertise of key users, adding more requirements and increasing standards may help push away from quick, easy approach.
- Community work should be budgeted in even if you are on soft money, recognizing these efforts as just as important
- Software engineering tasks should be factored into grant/proposal application itself

### Diagnostic Packages

Will ESDS be herding the existing diagnostic package development? How will ESDS bring these packages together?

- We will run the evolution backwards, and see how they coalesce, avoiding duplication of effort though communicating with each other about what we have done, challenges we face.
- An example of this is pop-tools, which provides a framework for other groups to follow.

### Overall Design

What was the original motivation and design of the Pangeo Projection and how does that relate to the design of this initiative?

- The goal was to enable a new form of scientific inquiry, taking away the toil of data processing and management and to allow scientists to explore and use data more efficiently. The focus has been on enabling scalable, reproducible, and open tools for working with geoscientific data
- Yes, there will be some growing pains an associated learning curve, but the curve is typically quick and efficiency gains are real

### Transparency of Models and Data

If we keep abstracting further from the underlying data and models, aren’t we in a real danger of disconnecting from what the models and data actually mean? Don’t we view the world simply through the world through the lens of the tools and libraries that have been written by other people? Is there a way in which we can ensure that the limitation of models, data, and analysis methods being provided can be explicit and transparent to researchers using them?

### Interactive Computing

What is 2i2c?

- Check out the website! [2i2c site](http://2i2c.org/)

### Usability of Tools

How do we make tools such as dask, xarray, etc. available to people in a simple way? Previous experience suggeests that you could have a great tool but it is not used easily and requires lots of complex dependencies to start.

- There are default conda environments that include the Pangeo stack in the CESM-container, as well as on Casper/Cheyenne
- Make sure that tutorials are setup in a containerized, simple environment
- A more detailed tutorial on setting up your own environment on Cheyenne/Casper is needed

### Pop-Tools

What data format does pop-tools work with?

- Supports Xarray input - so anything that Xarray supports (ex. netCDF, HDF, etc.)
- Xaray also provides an abstraction of the data, so all 100s+ GB/TB of data are not read in at a single time, making it scalable

### Parallel Writing/Zarr

Dask/Xarray can be a pain to use when writing files and can be slow. Is there a parallel writing ability?

- Writing in parallel to netCDF can be a pain due to HDF5, writing to zarr then converting to netcdf is preferred.
- Moving to Zarr in the future will be the way to go - it is much faster, especially on cloud computing platforms

### Shifting Landscape of Technical Tools

What happens in 5 years when Julia or Ruby becomes the language de jour?

- We can make decision in 5 years
- We do a lot of numerical work and analysis. In terms of this framework, programming languages and analysis tools are our lab equipment. Lab equipment gets upgraded, and scientists worldwide need to keep up.

Additional questions? Feel free to submit an issue on [Github](https://github.com/NCAR/esds/issues)
