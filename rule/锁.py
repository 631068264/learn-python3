#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author = 'wyx'
@time = 2016/12/7 22:07
@annotation = '' 
"""

# class SharedCounter:
#     '''
#     A counter object that can be shared by multiple threads.
#     '''
#
#     def __init__(self, initial_value=0):
#         self._value = initial_value
#         self._value_lock = threading.Lock()
#
#     def incr(self, delta=1):
#         '''
#         Increment the counter with locking
#         '''
#         with self._value_lock:
#             self._value += delta
#
#     def decr(self, delta=1):
#         '''
#         Decrement the counter with locking
#         '''
#         with self._value_lock:
#             self._value -= delta

import threading
from contextlib import contextmanager

# Thread-local state to stored information on locks already acquired
_local = threading.local()
"""
可使用 thread.local() 创建一个本地线程存储对象。
对这个对象的属性的保存和读取操作都只会对执行线程可见，
而其他线程并不可见。
"""


@contextmanager
def acquire(*locks):
    # Sort locks by object identifier
    locks = sorted(locks, key=lambda x: id(x))

    # Make sure lock order of previously acquired locks is not violated
    acquired = getattr(_local, 'acquired', [])
    if acquired and max(id(lock) for lock in acquired) >= id(locks[0]):
        raise RuntimeError('Lock Order Violation')

    # Acquire all of the locks
    acquired.extend(locks)
    _local.acquired = acquired

    try:
        for lock in locks:
            lock.acquire()
        yield
    finally:
        # Release locks in reverse order of acquisition
        for lock in reversed(locks):
            lock.release()
        del acquired[-len(locks):]


import threading

x_lock = threading.Lock()
y_lock = threading.Lock()


def thread_1():
    while True:
        with acquire(x_lock, y_lock):
            print('Thread-1')


def thread_2():
    while True:
        with acquire(y_lock, x_lock):
            print('Thread-2')


t1 = threading.Thread(target=thread_1)
t1.daemon = True
t1.start()

t2 = threading.Thread(target=thread_2)
t2.daemon = True
t2.start()
