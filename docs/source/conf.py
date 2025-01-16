import sys
import os

sys.path.insert(0, os.path.abspath("../.."))


# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "ArcadeMachine"
copyright = "2024, ColapsChair"
author = "ColapsChair"
release = "0.1"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
]

templates_path = ["_templates"]
exclude_patterns = [
    "games/**/assets/**",  # Exclude all assets directories and their contents
    "games/**/font/**",  # Exclude all font directories
    "games/**/pics/**",  # Exclude all pics directories
    "games/**/sounds/**",  # Exclude all sounds directories
    "games/**/graphics/**",  # Exclude all graphics directories
    "games/**/Visuals_Readme/**",  # Exclude all Visuals_Readme directories
    "games/**/sprites/**",  # Exclude all sprites directories
    "games/**/challenge_pictures/**",  # Exclude all challenge_pictures directories
    "games/**/maps/**",  # Exclude all maps directories
    "venv/**",  # Exclude virtual environment directory
    "*.md",  # Exclude markdown files
    "*.json",  # Exclude JSON files
    "*.txt",  # Exclude text files
    "requirements.txt",  # Exclude requirements.txt
    "games/**/__init__.py",  # Exclude __init__.py files
]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
html_theme = "furo"

html_static_path = ["_static"]
