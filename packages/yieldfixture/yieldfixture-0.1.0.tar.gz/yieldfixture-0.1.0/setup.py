# -*- coding:utf-8 -*-

import os
import sys

from setuptools import setup, find_packages
here = os.path.abspath(os.path.dirname(__file__))
try:
    with open(os.path.join(here, 'README.rst')) as f:
        README = f.read()
    with open(os.path.join(here, 'CHANGES.txt')) as f:
        CHANGES = f.read()
except IOError:
    README = CHANGES = ''

install_requires = []

docs_extras = []

tests_require = []

testing_extras = tests_require + []

setup(
    name='yieldfixture',
    version='0.1.0',
    description='-',
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    keywords='',
    author="podhmo",
    author_email="ababjam61+github@gmail.com",
    url="https://github.com/podhmo/yieldfixture",
    packages=find_packages(exclude=["yieldfixture.tests"]),
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    extras_require={
        'testing': testing_extras,
        'docs': docs_extras,
    },
    tests_require=tests_require,
    test_suite="yieldfixture.tests",
    entry_points="""
"""
)
