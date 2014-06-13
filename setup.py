#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='blanc-basic-news',
    version='0.3',
    description='Blanc Basic News for Django',
    long_description=open('README.rst').read(),
    url='https://github.com/blancltd/blanc-basic-news',
    maintainer='Alex Tomkins',
    maintainer_email='alex@blanc.ltd.uk',
    platforms=['any'],
    install_requires=[
        'blanc-basic-assets>=0.3',
    ],
    packages=find_packages(),
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
    ],
    license='BSD',
)
