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
from os import path

root = path.realpath(path.join(path.dirname(__file__), "..", ".."))
sys.path.insert(1, root)
# sys.path.insert(0, os.path.abspath("."))


# -- Project information -----------------------------------------------------

project = "okama"
copyright = "2021, MBK Development LLC"
author = "Sergey Kikevich"

# The full version, including alpha/beta/rc tags
# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
# import okama  # isort:skip

# version = '%s r%s' % (pandas.__version__, svn_version())
version = 1.0.0

# The full version, including alpha/beta/rc tags.
release = 1.0.0

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
language = "en"

# -- General configuration ---------------------------------------------------

autodoc_default_flags = ["members"]
autosummary_generate = ["index"]

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "recommonmark",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.doctest",
    # "sphinx.ext.napoleon",
    "numpydoc",  # handle NumPy documentation formatted docstrings instead of napoleon
    "sphinx.ext.mathjax",
    "sphinx_rtd_theme",
    "nbsphinx",
]

# source_suffix = '.rst'
# source_suffix = ['.rst', '.md']

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"
# html_theme = "pydata_sphinx_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
# html_theme_options = {
#     "external_links": [],
#     # "github_url": "https://github.com/mbk-dev/okama",
#     # "twitter_url": "https://twitter.com/pandas_dev",
#     # "google_analytics_id": "UA-27880019-2",
# }

# If false, no module index is generated.
html_use_modindex = True

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# -- Options for typehints ------------------------------------------------

# This value controls how to represents typehints.
autodoc_typehints = "none"

# -- Options for numpydoc ------------------------------------------------
numpydoc_attributes_as_param_list = False
numpydoc_show_class_members = False

# -- Options for nbsphinx ------------------------------------------------

# nbsphinx do not use requirejs (breaks bootstrap)
nbsphinx_requirejs_path = ""

# # Napoleon settings
# napoleon_google_docstring = False
# napoleon_numpy_docstring = True
# napoleon_include_init_with_doc = False
# napoleon_include_private_with_doc = False
# napoleon_include_special_with_doc = False
# napoleon_use_admonition_for_examples = False
# napoleon_use_admonition_for_notes = False
# napoleon_use_admonition_for_references = False
# napoleon_use_ivar = False
# napoleon_use_param = True
# napoleon_use_rtype = True
# napoleon_type_aliases = None
# napoleon_attr_annotations = True

# The encoding of source files.
source_encoding = "utf-8"
