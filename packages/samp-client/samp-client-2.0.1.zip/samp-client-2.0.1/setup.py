#!/usr/bin/env python
from distutils.core import setup


setup(
    name='samp-client',
    version='2.0.1',
    packages=['samp_client'],
    url='https://github.com/mick88/samp-client',
    license='MIT',
    author='Michal Dabski',
    author_email='contact@michaldabski.com',
    requires=['future'],
    description='SA-MP API client for python supporting both query and RCON APIs',
    long_description=open('README.md', 'r').read(),
)
