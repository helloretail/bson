#!/usr/bin/env python
# vim: set fileencoding=utf8 shiftwidth=4 tabstop=4 textwidth=80 foldmethod=marker :
# Copyright (c) 2010, Kou Man Tong. All rights reserved.
# Copyright (c) 2015, Ayun Park. All rights reserved.
# For licensing, see LICENSE file included in the package.
import sys
import pkgutil
from setuptools import setup
from setuptools.command.install import install

setup(
    name="hrbson",
    version="0.5.10",
    packages=["hrbson"],
    install_requires=["python-dateutil>=2.4.0", "six>=1.9.0"],
    author="Ayun Park",
    author_email="iamparkayun@gmail.com",
    description="BSON codec for Python",
    long_description="""Independent BSON codec for Python that doesn't depend on MongoDB.""",
    platforms="Any",
    license="BSD",
    keywords="BSON codec",
    url="http://github.com/helloretail/hrbson",
    classifiers=[
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ]
)
