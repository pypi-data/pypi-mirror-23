#  -*- coding: utf-8 -*-
"""
Setuptools script for the Django Generic Counter app.
"""

import os

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages


open_local = lambda path: open(os.path.join(os.path.dirname(__file__), path))

config = {
    "name": "django-generic-counter",
    "version": "0.0.9",
    "namespace_packages": [],
    "packages": find_packages(exclude=[
        "*.tests",
       "*.tests.*",
       "tests.*",
       "tests",
       "*.ez_setup",
       "*.ez_setup.*",
       "ez_setup.*",
       "ez_setup",
       "*.examples",
       "*.examples.*",
       "examples.*",
       "examples"
    ]),
    "include_package_data": True,
    "package_data": {"": ["*.js"], },
    "scripts": [],
    "entry_points": {},
    "install_requires": open_local("requirements.txt").readlines(),
    "tests_require": open_local("test-requirements.txt").readlines(),
    "test_suite": 'nose.collector',
    "zip_safe": False,
    # Metadata for upload to PyPI
    "author": 'Ellis Percival',
    "author_email": "ellis@0x07.co.uk",
    "description": open_local("README.rst").read(),
    "classifiers": ["Programming Language :: Python", ],
    "license": "",
    "keywords": "",
    "url": "",
}

setup(**config)
