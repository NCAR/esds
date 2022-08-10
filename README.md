# [ncar.github.io/esds](https://ncar.github.io/esds/)

![GitHub Workflow Status (branch)](https://img.shields.io/github/workflow/status/NCAR/esds/deploy-website/main?logo=github&style=for-the-badge)

Repository for hosting material related to Earth System Data Science Initiative efforts. The contents are posted at [ncar.github.io/esds](https://ncar.github.io/esds/).

## Tips for Building the Site Locally

To preview your changes to the site, you will have to build the site locally.
To do that you need to:

1. Create the conda environment for this repository with `conda env create -f environment.yml`.
2. Activate your environment with `conda activate esds-blog`
3. And build the site with `make html`

At this point you can preview your built site with your prefered method. Here are some options:

1. Navigating to `_build/index.html` and opening in your prefered Browser (often possible with a right click).
2. View via localhost by using Python `python -m SimpleHTTPServer`
3. Or view via localhost by using Node js with `npm install http-server -g` and `http-server name-of-file`

**NOTE:** If you added a file, it must be represented in the Table of Contents `toctree` within the `index.md` file to be built with the site.
