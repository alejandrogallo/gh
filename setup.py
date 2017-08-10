# -*- coding: utf-8 -*-
#
# you can install this to a local test virtualenv like so:
#   virtualenv venv
#   ./venv/bin/pip install --editable .
#   ./venv/bin/pip install --editable .[dev]  # with dev requirements, too

from __future__ import print_function

from setuptools import setup

from gh import __version__


setup(
    name='gh',
    version=__version__,
    maintainer='Alejandro Gallo',
    maintainer_email='aamsgallo@gmail.com',
    license='LGPL',
    url='https://github.com/alejandrogallo/gh',
    install_requires=[
       "argcomplete",
       "configparser",
       "argparse",
       "PyYAML",
        ],
    extras_require=dict(
        dev=[]
    ),

    description='Simple program to search github',
    long_description='Simple program to search github',
    keywords=[
        'cli',
        'github'
        ],
    packages=[
        "gh",
        "gh.commands"
    ],
    test_suite="gh.tests",
    entry_points=dict(
        console_scripts=[
            'gh=gh.gh:main'
        ]
    ),

    platforms=['any'],
)
