#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author = 'wyx'
@time = 2018/7/4 16:58
@annotation = ''
"""
import multiprocessing



def work(filename, max_count):
    lock = lockfile.FileLock(filename)
    for n in range(max_count):
        f = open(filename, "w+b")
        try:
            nbr = int(f.read().decode())
        except ValueError as err:
            print("File is empty, starting to count from 0, error: " + str(err))
            nbr = 0
        # f = open(filename, "w")
        f.write(str(nbr + 1).encode())
        f.close()


if __name__ == "__main__":
    max_worker = 4
    filename = 'a.txt'
    max_count = 100
    processes = []
    for i in range(max_worker):
        process = multiprocessing.Process(target=work, args=(filename, max_count))
        process.start()
        processes.append(process)
    for p in processes:
        p.join()
