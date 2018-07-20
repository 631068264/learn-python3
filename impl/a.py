#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author = 'wyx'
@time = 2018/7/19 11:00
@annotation = ''
"""
import random
import time
from contextlib import contextmanager
import importlib

PATH = 'impl.%s'
def import_mod(mod_name):
    try:

        return importlib.import_module(mod_name)
    except Exception as e:
        pass


@contextmanager
def reload_mod(mod_name):
    import sys
    mod = import_mod(mod_name)
    try:
        yield mod
    finally:
        sys.modules.pop(mod_name, None)


while True:
    path = PATH % 'b'

    # mod = import_mod(path)
    # print(mod.B().a)

    # with reload_mod(path) as mod:
    #     print(mod.B().a)


    mod = import_mod(path)
    mod = importlib.reload(mod)
    print(mod.B().a)
    time.sleep(random.randint(1,10)*0.01)