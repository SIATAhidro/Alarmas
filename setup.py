#!/usr/bin/env python
import os
from numpy.distutils.core import setup, Extension

setup(
    name='hidro_alarmas',
    version='0.0.1',
    author='Hidro SIATA',
    author_email='hidrosiata@gmail.com',    
    packages=['alarmas'],
    package_data={'alarmas':['ensayo.py']},
    url='https://github.com/SIATAhidro/Alarmas.git',
    license='LICENSE.txt',
    description='Montaje de alarmas',
    long_description=open('README.md').read(),
    install_requires=[ ],
    )
