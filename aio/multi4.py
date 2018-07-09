#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author = 'wyx'
@time = 2018/7/4 16:58
@annotation = ''
"""
import multiprocessing
import time


def add(queue, value, lock, pro_name):
    # with lock:
    number = queue.get()
    print("{} init {} {}".format(pro_name, number, value))
    # print("{} init {} {}".format(pro_name, number.value, value))
    for i in range(1, 6):
        number += value
        # number.value += value
        time.sleep(1)
        print("{} {} {}".format(pro_name, number, value))
        # print("{} {} {}".format(pro_name, number.value, value))

    print('{} {}'.format(pro_name, number))

    # print('{} {}'.format(pro_name, number.value))
    queue.put(number)

if __name__ == "__main__":
    lock = multiprocessing.Lock()
    number = multiprocessing.Queue()
    number.put(0)
    p1 = multiprocessing.Process(target=add, args=(number, 1, lock, 'pro_1'))
    p2 = multiprocessing.Process(target=add, args=(number, 3, lock, 'pro_2'))
    p1.start()
    p2.start()
    print("main end")
