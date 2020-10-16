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
import os
import sys
sys.path.insert(0, os.path.abspath('.'))
from better import better_theme_path

# -- Project information -----------------------------------------------------

project = 'North Africa Land Degradation Monitoring Service'
copyright = '2020, Derick Ongeri'
author = 'Derick Ongeri'

# The full version, including alpha/beta/rc tags
release = '0.0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.


extensions = [

]


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'alabaster'
html_theme_path = [better_theme_path]
html_theme = "better"

html_sidebars = { '**': ['globaltoc.html', 'relations.html', 'sourcelink.html', 'searchbox.html'] }


html_theme_options = {
    # show sidebar on the right instead of on the left
	'rightsidebar': False,
	# inline CSS to insert into the page if you're too lazy to make a
	# separate file
	'inlinecss': '',
	# CSS files to include after all other CSS files
	# (refer to by relative path from conf.py directory, or link to a
	# remote file)
	'cssfiles': ['_static/my_style.css'], # default is empty list
	# show a big text header with the value of html_title
	'showheader': True,
	# show the breadcrumbs and index|next|previous links at the top of
	# the page
	'showrelbartop': True,
	# same for bottom of the page
	'showrelbarbottom': True,
	# show the self-serving link in the footer
	'linktotheme': True,
	# width of the sidebar. page width is determined by a CSS rule.
	# I prefer to define things in rem because it scales with the
	# global font size rather than pixels or the local font size.
	'sidebarwidth': '15rem',
	# color of all body text
	'textcolor': '#000000',
	# color of all headings (<h1> tags); defaults to the value of
	# textcolor, which is why it's defined here at all.
	'headtextcolor': '',
	# color of text in the footer, including links; defaults to the
	# value of textcolor
	'footertextcolor': '',
	# Google Analytics info
	'ga_ua': '',
	'ga_domain': '',
	}

html_theme_options['cssfiles'] = ['_static/style.css']
#html_theme_path = []
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
