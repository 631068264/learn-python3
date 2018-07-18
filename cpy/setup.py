#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author = 'wyx'
@time = 2018/7/13 15:15
@annotation = ''
"""
from distutils.core import setup

from Cython.Build import cythonize

setup(ext_modules=cythonize('*.pyx'))
