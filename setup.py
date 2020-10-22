#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from pathlib import Path

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == "publish":
    os.system("python setup.py sdist upload")
    sys.exit()


readme = Path("README.rst").read_text()
history = Path("HISTORY.rst").read_text().replace(".. :changelog:", "")

requires = [
    "sarge",
    "structlog",
    "requests",
    "beautifulsoup4",
    "URLObject",
    "NLTK",
    "textblob",
    "networkx",
    "pydot",
]

setup(
    name="wrdrd",
    version="0.2.0",
    description="WRD R&D Web Consulting Tools and Documentation",
    long_description=readme + "\n\n" + history,
    author="Wes Turner",
    author_email="wes@wrd.nu",
    url="https://bitbucket.org/westurner/wrdrd",
    packages=["wrdrd",],
    package_dir={"wrdrd": "wrdrd"},
    include_package_data=True,
    install_requires=requires,
    license="",
    zip_safe=False,
    keywords="wrdrd",
    classifiers=["Natural Language :: English",],
    test_suite="tests",
    entry_points={
        "console_scripts": [
            "domaintool = wrdrd.tools.domain:main",
            "crawl = wrdrd.tools.crawl:main",
            "stripsinglehtml = wrdrd.tools.stripsinglehtml:main",
        ]
    },
)
