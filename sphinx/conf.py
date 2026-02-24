# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import os
import sys
import re
import inspect
from datetime import datetime

from xtal_code import __version__ as xtl_version
from numpydoc.docscrape_sphinx import SphinxDocString

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# sys.path.insert(0, os.path.abspath("."))
sys.path.append("../")

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Consistent Crystal Conventions'
copyright = '2026, Austin Gerlt'
author = 'Austin Gerlt'
release = xtl_version
html_title = 'Consistent Xtals'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "matplotlib.sphinxext.plot_directive",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.doctest",
    "sphinx.ext.imgconverter",
    "sphinx_design",
    "sphinx_gallery.gen_gallery",
    "numpydoc",  # Must be loaded after autodoc
]
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    # Suppress warnings from Sphinx regarding "duplicate source files":
    "examples/*/*.ipynb",
    "examples/*/*.py",
    "conventions/*/*.ipynb",
    "conventions/*/*.py",
    "*.code_workspace",
]

# TODO: maybe add intersphinx mapping?


# HTML theming: pydata-sphinx-theme
# https://pydata-sphinx-theme.readthedocs.io
html_theme = "pydata_sphinx_theme"
html_theme_options = {
    "github_url": "https://github.com/argerlt/Consistent-Crystal-Conventions",
    "header_links_before_dropdown": 6,
    "navigation_with_keys": True,
    "show_toc_level": 2,
}
html_static_path = ["_static"]

#TODO: maybe get logo?


# TODO: Bibtex? # https://sphinxcontrib-bibtex.readthedocs.io
# TODO:sphinx-codeautolink?

# -- sphinx.ext.autodoc
# https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html
autosummary_ignore_module_all = False
autosummary_imported_members = True
autodoc_typehints_format = "short"
autodoc_default_options = {
    "show-inheritance": True,
}

#TODO: NumpyDoc?

# -- matplotlib.sphinxext.plot_directive
# https://matplotlib.org/stable/api/sphinxext_plot_directive_api.html
plot_formats = ["png"]
plot_html_show_source_link = False
plot_html_show_formats = False
plot_include_source = True


def _str_examples(self):
    examples_str = "\n".join(self["Examples"])
    if (
        self.use_plots
        and (
            re.search(r"\b(.plot)\b", examples_str)
            or re.search(r"\b(.plot_map)\b", examples_str)
            or re.search(r"\b(.imshow)\b", examples_str)
        )
        and "plot::" not in examples_str
    ):
        out = []
        out += self._str_header("Examples")
        out += [".. plot::", ""]
        out += self._str_indent(self["Examples"])
        out += [""]
        return out
    else:
        return self._str_section("Examples")


SphinxDocString._str_examples = _str_examples

html_sidebars = {
    "index": ["sidebar-nav-bs", "sidebar-ethical-ads"],
   "**": ["sidebar-nav-bs", "sidebar-ethical-ads"]
}
# -- Sphinx-Gallery
# https://sphinx-gallery.github.io
sphinx_gallery_conf = {
    "backreferences_dir": "reference/generated",
    "examples_dirs": ["../examples","../conventions"],
    "filename_pattern": "^((?!sgskip).)*$",
    "gallery_dirs": ["examples", "conventions"],
}
autosummary_generate = True
