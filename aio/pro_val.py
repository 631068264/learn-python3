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


def add(number, value, lock, pro_name):
    # with lock:
    # print("{} init {} {}".format(pro_name, number, value))
    print("{} init {} {}".format(pro_name, number.value, value))
    for i in range(1, 6):
        # number += value
        # print("B {} {} {}".format(pro_name, number.value, value))
        # if number.value > 11:
        #     break
        with number.get_lock():
            number.value += value
        time.sleep(random.randint(1,10)*0.0001)
        # print("{} {} {}".format(pro_name, number, value))
        print("{} {} {}".format(pro_name, number.value, value))

    # print('{} {}'.format(pro_name, number))
    print('{} {}'.format(pro_name, number.value))


if __name__ == "__main__":
    lock = multiprocessing.Lock()
    # number = 0
    number = multiprocessing.Value('i', 0)
    p1 = multiprocessing.Process(target=add, args=(number, 1, lock, 'pro_1'))
    p2 = multiprocessing.Process(target=add, args=(number, 3, lock, 'pro_2'))
    p1.start()
    p2.start()
    print("main end")
