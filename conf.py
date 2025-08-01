# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'ESDS Website'
copyright = '2021, ESDS Community'
author = 'ESDS Community'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'myst_nb',
    'ablog',
    'sphinxext.rediraffe',
    'sphinx_design',
    'sphinx_copybutton',
]

# sphinx-copybutton configurations
copybutton_prompt_text = r'>>> |\.\.\. |\$ |In \[\d*\]: | {2,5}\.\.\.: | {5,8}: '
copybutton_prompt_is_regexp = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Set language which will propagate to the top-level HTML tag
language = 'en'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

html_logo = "_static/esds_logo.png"
html_favicon = "_static/esds_logo.png"
html_sourcelink_suffix = ""
html_last_updated_fmt = ""

html_context = {
    "github_user": "NCAR",
    "github_repo": "esds",
    "github_version": "main",
    "doc_path": "",
}

html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_show_sourcelink = False

html_theme = 'pydata_sphinx_theme'

# Add some more theme Options
html_theme_options = {
    'use_edit_page_button': True,
    'github_url': 'https://github.com/NCAR/esds',
    'navbar_end': ['theme-switcher', 'navbar-icon-links'],
    'icon_links': [
        {
            "name": "YouTube",
            "url": "https://www.youtube.com/@ncar_ucar_esds",
            "icon": "fa-brands fa-square-youtube",
            "type": "fontawesome",
        },
    ],
}

html_theme_options["analytics"] = {
    "google_analytics_id": "UA-196809533-1",
}

rediraffe_redirects = 'redirects.txt'


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

html_sidebars = {
    'index': ['hello.html'],
    'about': ['hello.html'],
    'communication': ['hello.html'],
    'office-hours': ['hello.html'],
    'resources': ['hello.html'],
    'blog': ['ablog/recentposts.html', 'ablog/archives.html', 'ablog/tagcloud.html'],
    'posts/**': ['ablog/postcard.html', 'ablog/recentposts.html', 'ablog/archives.html'],
}


blog_baseurl = 'ncar.github.io/esds/'
blog_title = 'ESDS'
blog_path = 'blog'
fontawesome_included = True
blog_post_pattern = 'posts/*/*'
post_redirect_refresh = 1
post_auto_image = 1
post_auto_excerpt = 2

# Panels config
panels_add_bootstrap_css = False

# MyST config
myst_enable_extensions = ['amsmath', 'colon_fence', 'deflist', 'html_image', 'dollarmath']
myst_url_schemes = ['http', 'https', 'mailto']

# Temporarily stored as off until we fix it
nb_execution_mode = 'off'

