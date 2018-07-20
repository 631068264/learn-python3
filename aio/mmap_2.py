#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author = 'wyx'
@time = 2018/7/4 16:58
@annotation = ''
"""
import multiprocessing
import time
from mmap import mmap


def add(mm, value, lock, pro_name):
    with lock:
        mm.seek(0)
        number = mm.read(1)
        number = int(number.decode())

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
        mm.seek(0)
        print(number)
        mm.write(str(number).encode())


if __name__ == "__main__":
    lock = multiprocessing.Lock()
    with open('mmap.txt', 'r+b') as f:
        with mmap(f.fileno(), 2) as mm:
            mm.write(str(0).encode())
            p1 = multiprocessing.Process(target=add, args=(mm, 1, lock, 'pro_1'))
            p2 = multiprocessing.Process(target=add, args=(mm, 3, lock, 'pro_2'))
            p1.start()
            p2.start()

            p1.join()
            p2.join()
            print("main end")
            mm.seek(0)
            d = mm.read().decode()
            print(d)
            print(type(d))
