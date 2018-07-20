#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author = 'wyx'
@time = 2018/7/3 22:45
@annotation = ''
"""
import random
import time
from concurrent.futures import ProcessPoolExecutor


def csdf(name):
    print('Strart 啦啦' + name)
    sec = random.uniform(0, 3)
    time.sleep(sec)
    print('{}:{}'.format(sec, name))
    return name


worker = 10
names = list('QWERTYUIOPASDFGHJKLZXCVBNM')


def pro_pool_1():
    with ProcessPoolExecutor(worker) as executor:
        futures = [executor.submit(csdf, n) for n in names]
        print(futures)
        results = [f.result() for f in futures]

        # results = wait(futures, 20)

        # 有序
        print(results)


def pro_pool_2():
    with ProcessPoolExecutor(worker) as executor:
        for r in executor.map(csdf, names):
            # 先到先得
            print(r)
