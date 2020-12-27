# BOTLIB - pure python3 bot library
#
# this file is place in the public domain

"library to program bots"

import os

from setuptools import setup

def read():
    return open("README.rst", "r").read()

setup(
    name='botdev',
    version='2',
    url='https://github.com/bthate/botdev',
    author='Bart Thate',
    author_email='bthate@dds.nl', 
    description="BOTLIB development",
    long_description=read(),
    license='Public Domain',
    classifiers=['Development Status :: 4 - Beta',
                 'License :: Public Domain',
                 'Operating System :: Unix',
                 'Programming Language :: Python',
                 'Topic :: Utilities'
                ]
)
