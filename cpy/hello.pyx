#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author = 'wyx'
@time = 2018/7/13 15:32
@annotation = ''
"""

# def fibc(n):
#     a, b = 0.0, 1.0
#     for i in range(n):
#         a, b = a + b, a
#     return a

def fib(n):
    cdef double a = 0.0, b = 1.0
    for i in range(n):
        a, b = a + b, a
    return a
