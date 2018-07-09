#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author = 'wyx'
@time = 2018/7/6 16:47
@annotation = ''
"""
import time
from functools import wraps
from math import sqrt


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print('{} run {} sec'.format(func.__name__, end - start))
        return res

    return wrapper


prime = [112272535095295, 100109100129100369, 100109100129101027, 100109100129100151, 100109100129162907]


@timer
def check_prime(n):
    if n % 2 == 0:
        return False
    from_i = 3
    to_i = sqrt(n) + 1
    for i in range(from_i, int(to_i), 2):
        if n % i == 0:
            return False
    return True


def r(func):
    for p in prime:
        print(func(p))


r(check_prime)
