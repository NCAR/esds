---
date: 2019-12-09
tags: open source, open development
author: Kevin Paul
---

# We are Xdev!

More than a year ago, [Matthew Long](http://www.cgd.ucar.edu/staff/mclong/) and
[I](https://staff.ucar.edu/users/kpaul) started shopping around the idea that a
lot of what we do here at [NCAR](https://ncar.ucar.edu/), as well as _how_ we do
it, needed a bit of a facelift. Our pitch was simple: As an institution that
supports the geoscientific community by providing valuable datasets, supercomputing
facilities, and computer models, NCAR needs to _exemplify_ modern best practices
in the _development_ and _use_ of these resources. We took inspiration from the
remarkably effective [Pangeo](https://pangeo.io) community, which continues to show
enormous success with Open Source development when coupled with modern software
best practices, and we started to develop a plan of how to help shift, albeit
slowly, both NCAR and---though collaboration with the Pangeo community---the
geoscience community toward a better future.

To implement our plan, Matt and I started to see how much benefit to NCAR it could
be to have a small, Agile team that was dedicated to prototyping new technologies
for the benefit of the rest of the organization and the rest of the geoscience
community, as a whole, like the [UK Met Office](https://www.metoffice.gov.uk/)'s
[Informatics Lab](https://www.informaticslab.co.uk/). However, instead of just
churning out technology, this group would also serve as an example to the rest of
NCAR on how (and why) to use modern best practices (GitHub, continuous integration,
test-driven development, etc.) for scientific software development. ...and for
science itself!

Matt and I dreamed big, and as usually happens when the reality of budgets collides
with dreams, we were forced to scale back our vision of a ten-person team to small
group of two. Two is still greater than zero, so we considered that a success, and
the Experimental Development Team (Xdev) was born! In October of 2018,
[Anderson Banihirwe](https://andersonbanihirwe.dev/) joined the team as a member of
NCAR's [Computational & Informatics Laboratory (CISL)](https://www2.cisl.ucar.edu/),
and in January of 2019, [Julia Kent](https://staff.ucar.edu/users/jkent) (CISL)
joined us, too. By the fall of 2019, we were able to bolster our ranks with
part-time support from [Brian Bonnlander](https://staff.ucar.edu/users/bonnland)
(CISL), [Michael Levy](https://staff.ucar.edu/users/mlevy) (CGD), and
[Mohammad Abouali](https://staff.ucar.edu/users/mabouali) (CISL). Read more about
us [here](https://ncar.github.io/xdev/pages/about/).

Currently, the Xdev Team is working to make _curiousity-driven analysis_ of "big"
scientific data a day-to-day reality. This is a tall order! Not only does the
technology need to advance to make such a dream a reality, but helping users
(_i.e._, scientists) fully understand this new paradigm is extremely challenging.
We appreciate that many scientists do not want to become developers themselves,
which means that we must promote technology that is _expressive_, letting the user
do more science with less engineering. This means _abstracting_ away computational
details, such as parallelism (_e.g._, with [Dask](https://dask.org)) or I/O (_e.g._,
with [Xarray](https://xarray.pydata.org/en/stable/)) or complex scientific
functions, without abstracting away so much that the user can no longer problem
solve when things go wrong. We believe that means using the Python programming
language. Python is designed for rapid prototyping, which is the nature of most
scientific programming for analysis purposes.

Achieving this goal also means _teaching_ scientists about a new way of performing
and _thinking about_ data analysis. And this means not only teaching scientists
how to use the technology (_e.g._, giving tutorials, providing online examples,
_etc._), but also how the technology can improve science (_e.g._, by making their
workflows reproducible or replicable, by letting scientists ask questions they
couldn't with unscalable legacy tools, _etc._).

So, the Xdev Teams works with scientists to develop new technology, promotes
existing technology, and teaches scientists how to use this technology for the
greatest good. This is who we are, and we are just beginning to scratch the
surface on a very big problem.
