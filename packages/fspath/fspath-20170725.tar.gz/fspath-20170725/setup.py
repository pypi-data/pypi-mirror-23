#!/usr/bin/env python
# -*- coding: utf-8; mode: python -*-

import sys
import os
import platform
from setuptools import setup, find_packages

_dir = os.path.abspath(os.path.dirname(__file__))

sys.path.append(_dir)

import fspath

install_requires = [
    "six" ]

_which = "which.py"
if platform.system() == 'Windows':
    _which = "which.py"

setup(
    name               = "fspath"
    , version          = fspath.__version__
    , description      = fspath.__description__
    , long_description = fspath.__doc__
    , url              = fspath.__url__
    , author           = "Markus Heiser"
    , author_email     = "markus.heiser@darmarIT.de"
    , license          = fspath.__license__
    , keywords         = "path-names development"
    , packages         = find_packages(exclude=['docs', 'tests'])
    , install_requires = install_requires
    , entry_points     = {
        'console_scripts': [
            _which + ' = fspath._which:main'
            , 'fspath = fspath.main:main'
        ]}
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    , classifiers = [
        "Development Status :: 5 - Production/Stable"
        , "Intended Audience :: Developers"
        , "License :: OSI Approved :: GNU General Public License v2 (GPLv2)"
        , "Operating System :: OS Independent"
        , "Programming Language :: Python"
        , "Programming Language :: Python :: 2"
        , "Programming Language :: Python :: 3"
        , "Topic :: Utilities"
        , "Topic :: Software Development :: Libraries"
        , "Topic :: System :: Filesystems" ]
)
