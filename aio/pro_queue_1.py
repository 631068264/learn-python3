#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author = 'wyx'
@time = 2018/7/4 16:58
@annotation = ''
"""
import multiprocessing
import random
import time
from _queue import Empty


def get(queue, pro_name):
    num = 0
    while True:
        try:
            flag = queue.get(False)
        except Empty:
            flag = None

        print('{}-{}'.format(pro_name, flag))
        if flag:
            for i in range(1, 6):
                num += 1
                print("{} {}".format(pro_name, num))
        else:
            num = 0
            print('{} stop'.format(pro_name))
            break

        time.sleep(random.randint(1, 10) * 0.0001)


def put(queue, pro_name):
    q = [True] * 10 + [False] * 5
    while True:
        flag = random.choice(q)
        print('{}-{}'.format(pro_name, flag))
        queue.put(flag)


if __name__ == "__main__":
    lock = multiprocessing.Lock()
    queue = multiprocessing.Queue(1)
    p1 = multiprocessing.Process(target=get, args=(queue, 'pro_1'))
    p2 = multiprocessing.Process(target=put, args=(queue, 'pro_2'))
    p1.start()
    p2.start()
    # p1.join()
    # p2.join()
    print("main end")
