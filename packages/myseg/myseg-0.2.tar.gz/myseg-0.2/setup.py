#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='myseg',
    version='0.2',
    description='Command-line utility for searching and filtering videos based on objects that appear in them using convolutional neural networks',
    packages=['myseg'],
    scripts=['bin/myseg'],
    install_requires=[
        'pyPEG2>=2.15.1',
        'requests>=2.7.0',
        'moviepy>=0.2.2.11',
        'docopt>=0.6.2',
        'progressbar>=2.3',
        'numpy>=1.9.2',
        'pattern>=2.6',
        'termcolor>=1.1.0'
    ],
    license="MIT"
)
