#!/usr/bin/env python
# -*- coding: utf-8 -*-
import io
import re
from setuptools import setup

with io.open('drapion/__init__.py', 'rt', encoding='utf8') as f:
    version = re.search(r'__version__ = \'(.*?)\'', f.read()).group(1)

with io.open('README.md', 'rt', encoding='utf8') as f:
    readme = f.read()

setup(
    name='Drapion',
    description='A Simple library to facilitate consuming web API\'s',
    long_description=readme,
    version=version,
    url='https://github.com/giancarlopro/drapion',
    license='Apache 2.0',
    author='Giancarlo Rocha',
    author_email='giancarlorochapro@gmail.com',
    install_requires=[
        'requests>=2.9.1'
    ],
    python_requires='>=3.5',
    packages=['drapion'],
    include_package_data=True
)