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

setup(
    name='wrdsbc',
    version='0.1.0',
    description='WRD Small Business Consulting Tools and Documentation',
    long_description=readme + '\n\n' + history,
    author='Wes Turner',
    author_email='wes@wrd.nu',
    url='https://bitbucket.org/westurner/wrdsbc',
    packages=[
        'wrdsbc',
    ],
    package_dir={'wrdsbc': 'wrdsbc'},
    include_package_data=True,
    install_requires=[
    ],
    license="",
    zip_safe=False,
    keywords='wrdsbc',
    classifiers=[
        'Natural Language :: English',
    ],
    test_suite='tests',
)
