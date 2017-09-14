#!/usr/bin/env python

from setuptools import setup, find_packages
import py2ipynb

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='py2ipynb',
    version='0.1',
    description='Convert .py to .ipynb',
    long_description=readme,
    author='mishan88',
    author_email='mishanhideaki88@gmail.com',
    url='https://github.com/mishan88/py2ipynb.git',
    license=license,
    packages=find_packages(),
    entry_points={
        'console_scripts' : [
            'py2ipynb=py2ipynb.py2ipynb:main',
        ]
    },
    install_requires=['click', 'nbformat'],
    test_suite='tests'
 )
