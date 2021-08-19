---
author: Max Grover
date: 2021-4-2
tags: open-science, citation, software
---

# The Importance of Software Citation

One of the questions that came up during the [ESDS Town Hall](https://ncar.github.io/esds/posts/esds-blog/) was how do scientists/developers get credit toward their efforts in developing open-source code? Software that is used by the wider community should received the acknowledgment and recognition it deserves.

Data and academic publication citations have become popular in the literature, but often times, software is not cited... which can be arguably just as important to the work as the data.

The [NCAR Library team](https://library.ucar.edu/) put together a website, detailing software citation best practices, based on evaluating the >500 [NCAR Github Repositories](https://github.com/NCAR)

Here, we provide an overview of these recommendations, but if you are interested in more of the details, be sure to check out [the NCAR software citation documentation](https://ncar.github.io/software-citation/).

## How else should I make sure people cite my software?

Within your `README.md` document, be sure to add how you would like others to cite your work. For example, if your repository is for a specific paper, then provide the citation to that paper. If you would like people to cite the software itself, then be sure to specify that.

A great example of software citation instructions can be found on [Unidata's website](https://www.unidata.ucar.edu/community/index.html#acknowledge)

You can even add a DOI badge to your repository once you have one minted. An example is given below.

[![DOI](https://img.shields.io/badge/DOI-YOUR NCAR DOI)](https://doi.org/YOUR_NCAR_DOI)

## Why would I want a DOI?

DOI stands for "Digital Object Identifier" and serves as a permanent identifier of an article/document/or piece of software. Typically, it can be difficult to assign a DOI to software, especially since it can constantly be changing/evolving. Fortunately, through the NCAR Library, you can assign a DOI to your Github repository (although this is only available to NCAR produced and hosted software). The only requirements are the following

- Github repository link
- Minimum metadata
  - Creators, such as name/lab
  - Title of software
  - Publisher (ex. NCAR Github organization)
  - Publication year of software

## How do I mint a DOI for my repository if I am outside the NCAR organization?

Zenodo is a great option, and integrated within Github [Zenodo Plugin](https://guides.github.com/activities/citable-code/). This option can be good for people within the NCAR organization as well, especially if you would like to assign discrete DOIs to each of your releases.
