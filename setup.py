#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

requires = ['sh']

setup(
    name='wrdrd',
    version='0.1.0',
    description='WRD R&D Web Consulting Tools and Documentation',
    long_description=readme + '\n\n' + history,
    author='Wes Turner',
    author_email='wes@wrd.nu',
    url='https://bitbucket.org/westurner/wrdrd',
    packages=[
        'wrdrd',
    ],
    package_dir={'wrdrd': 'wrdrd'},
    include_package_data=True,
    install_requires=requires,
    license="",
    zip_safe=False,
    keywords='wrdrd',
    classifiers=[
        'Natural Language :: English',
    ],
    test_suite='tests',
    entry_points={
        'console_scripts': [
            'domaintool = wrdrd.tools.domain:main',
            'crawl = wrdrd.tools.crawl:main',
            'stripsinglehtml = wrdrd.tools.stripsinglehtml:main',
        ]
    }
)
