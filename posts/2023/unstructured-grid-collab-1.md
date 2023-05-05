---
author: Deepak Cherian, Katie Dagon, Falko Judt, Orhan Eroglu
date: 2023-05-05
tags: tutorial hackathon events
---

# Unstructured Grid Collaborative Work Time

ESDS hosted our first Collaborative Work Time event on April 17, 2023.
The topic of the session was "Working With Unstructured Grids".
Our goal is to encourage cross-lab collaboration and build lasting science-software partnerships.

The event was hybrid with in-person attendees in the Damon Room at the Mesa Lab.
A lucky overlap with the Improving Scientific Software conference, meant that collaborators from the Department of Energy were also able to attend in-person.

```{image} ../images/unstructured-grid-collab-1.jpg
:alt: Photo of unstructured grids collaborative work time session.
:width: 70%
:align: center
```

## Plan

Participants were asked to fill out a brief survey, and asked to self-organize by adding a one slide description of a project
to a [presentation](https://docs.google.com/presentation/d/1UDjNMMCyXcHRT6BvX_Lcs4AEoHpNM8LntEfxWOWwwNQ/edit#slide=id.p) in the weeks preceding the event.

At the event, we broke out in to approximately four groups. A recap from each group follows.

## Recap

#### Orhan Eroglu (CISL):

**Topic:** Project [Raijin](https://raijin.ucar.edu/) & [UXarray](https://uxarray.readthedocs.io/)

*What did your group do?*

The UXarray developers had a chance to discuss use cases and get feedback from the community members on UXarray. We branched into subgroups for different work ideas and coded with our users. We noticed a  significant bug related to face area calculations (Pull Request [#283](https://github.com/UXARRAY/uxarray/pull/283) and worked on that throughout the end of the day. We also worked on issues that came up with ingesting MPAS data into UXarray regarding attributes not being parsed with the dual mesh only (see pull requests [#274](https://github.com/UXARRAY/uxarray/pull/274) and [#275](https://github.com/UXARRAY/uxarray/pull/275)).

*Was it a fruitful experience?*

Very much!

*What worked for your group and what didn't work?*

Sitting together with the users and listening to their expectations was a great opportunity! Since we had multiple UXarray folks as facilitators, things worked quite well for us. That wouldn't happen if we didn't have that many helpers (as a side note for the future)

*Would it be useful to redo the  topic again?  What would you do differently the second time around?*

Yes, after some time. We'd add one or two work idea of our own group as well as those came from the community.


#### Falko Judt (MMM):

**Topic** Extract Tropical Cyclone Vitals from MPAS

*What did your group do?*

 Free discussion. Mostly scientist asking questions to the GeoCAT/UXarray experts. We didn't write any code because nobody had a project ready.

*Was it a fruitful experience?*

 Yes.

*What worked for your group and what didn't work?*

Discussion was great. Also just meeting some people face to face was a plus.

*Would it be useful to redo the  topic again?  What would you do differently the second time around?*

Yes, maybe in 1/2 year or so? Could tell people to have some project ready to get into some hands-on coding.


#### Katie Dagon (CGD):

**Topic**: Visualizing & Analyzing Community Atmosphere Model (CAM) with the spectral element (SE) grid output in Python

*What did your group do? Write code? discussions?*

We started with open discussion and sharing our experiences with the overall topic (CAM-SE analysis/visualization).
We then went through [a notebook](https://github.com/katiedagon/CAM-SE_analysis/blob/main/notebooks/CAM-SE.ipynb) I had prepared with various examples of remapping to visualize CAM-SE unstructured output.
I did a little live debugging, then [Deepak was kind enough](https://github.com/katiedagon/CAM-SE_analysis/pull/1) to help debug the xemsf code!
We ended with some additional discussion and had a few more participants log on after their first breakout sessions ended early.
In total I believe we had 9 active participants (myself included) and went for at least ~1.5 hours.

*Was it a fruitful experience?*

Yes, very. A lot of good information and helpful tips/tools were exchanged:
- Users need to consider different tools for different purposes (e.g., visualization, analysis, looking at extremes).
- Bilinear interpolation will change information but is generally acceptable when going from coarse to fine scale. Consider conservative remapping when going from fine to coarse scale, and nearest-neighbor method for preserving extremes.
- If you have access to NCAR HPC, CESM grid files are located at `/glade/p/cesmdata/cseg/inputdata/share/`
- [ncremap](https://github.com/nco/nco/blob/master/data/ncremap) via NCO tools is still a solid resource for remapping, though we are interested in Python-based alternatives.
- [VisIt](https://visit-dav.github.io/visit-website/index.html) and [ncvis](https://github.com/SEATStandards/ncvis) are useful for quick visualization of unstructured grids.
- [TempestRemap](https://github.com/ClimateGlobalChange/tempestremap) can be used for native spectral element regridding.
- Ongoing [UXarray development](https://github.com/UXARRAY/uxarray/issues/183) would hopefully make this process more seamless, so the user does not have to interact with the native grid. This is still in process.

*What worked for your group and what didn't work?*

Having an example notebook to walk through helped maintain the discussion, and once it got going we had plenty to discuss without coding. It helped that there were a few key participants present with a lot of expertise.
There were only two in-person participants, so technically we didn't need to be in the Damon room (and it was a little hard to hear at times with the overlapping group discussions in the same physical space). It would be nice to have more participants in person.

*Would it be useful to redo the  topic again?  What would you do differently the second time around?*

Perhaps, if there was enough interest. Maybe it would be good to have a tutorial-type notebook prepared for participants to live code together.


## Takeaways

- Would be good to have a prepared notebook to guide the project/discussion in addition to a single slide description
- In-person attendees enjoyed discussion, and encouraging more in-person participation would be helpful.
- A repeat in the future around the same topic would be valuable.
