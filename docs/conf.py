# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import suricata_check_extension_example

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "suricata-check"
copyright = "2024, Koen Teuwen"
author = "Koen Teuwen"

# Version / release information
version = suricata_check_extension_example.__version__
release = suricata_check_extension_example.__version__

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
    "autodoc2",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "sphinx_click",
]

templates_path = ["_templates"]
source_suffix = [".rst", ".md"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master", None),
    "idstools": ("https://idstools.readthedocs.io/en/latest/", None),
    "suricata-check": ("https://suricata-check.readthedocs.io/en/latest/", None),
}

root_doc = "index"
master_doc = "readme"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

# -- Options for Autodoc     -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#configuration
# https://sphinx-autodoc2.readthedocs.io/en/latest/index.html

# autoclass_context = "both"
# autodoc_class_signature = "seperated"
# autodoc_member_order = "groupwise"
# autodoc_default_flags = [
#     "members",
#     "special-members",
#     "inherited-members",
#     "show-inheritance",
#     "ignore-module-all",
#     "maxdepth",
# ]
# autodoc_default_options = {
#     "member-order": "bysource",
#     "special-members": "__init__",
#     "undoc-members": False,
#     "maxdepth": 2,
# }
# autodoc_typehints = "signature"
# autodoc_typehints_description_target = "all"

autodoc2_packages = [{"path": "../suricata_check_extension_example"}]
autodoc2_hidden_objects = ["undoc", "dunder", "private"]
autodoc2_class_docstring = "both"
autodoc2_docstrings = "all"
