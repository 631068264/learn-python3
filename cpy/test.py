#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author = 'wyx'
@time = 2018/7/13 15:37
@annotation = ''
"""
import pyximport

pyximport.install()

from cpy import hello
import time


def test_time(func, *args, **kwargs):
    s = time.time()
    func(*args, **kwargs)
    print(time.time() - s)


def fib(n):
    a, b = 0.0, 1.0
    for i in range(n):
        a, b = a + b, a
    return a


print(hello.__file__)
test_time(hello.fib, 90)
print()
test_time(fib, 90)
