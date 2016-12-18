#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author = 'wyx'
@time = 2016/12/7 21:33
@annotation = '' 
"""
"""
基于简单队列编写多线程程序在多数情况下是一个比较明智的选择。
从线程安全队列的底层实现来看，你无需在你的代码中使用锁和其他底层的同步机制，
这些只会把你的程序弄得乱七八糟。此外，使用队列这种基于消息的通信机制可以被扩展到更大的应用范畴

线程间通信实际上是在线程间传递对象引用。如果你担心对象的共享状态，
那你最好只传递不可修改的数据结构（如：整型、字符串或者元组）或者一个对象的深拷贝。

get() 和 put() 方法都支持非阻塞方式和设定超时

这些操作都可以用来避免当执行某些特定队列操作时发生无限阻塞的情况，比如，一个非阻塞的 put() 方法和一个固定大小的队列一起使用，这样当队列已满时就可以执行不同的代码。比如输出一条日志信息并丢弃。

def producer(q):
    ...
    try:
        q.put(item, block=False)
    except queue.Full:
        log.warning('queued item %r discarded!', item)

def consumer(q):
    while _running:
        try:
            item = q.get(timeout=5.0)
            # Process item
            ...
        except queue.Empty:
            pass
"""

# from queue import Queue
# from threading import Thread
#
#
# # A thread that produces data
# def producer(out_q, data):
#     while True:
#         # Produce some data
#         print("producer")
#         out_q.put(data)
#         break
#
#
# # A thread that consumes data
# def consumer(in_q):
#     while True:
#         # Get some data
#         print("consumer")
#         data = in_q.get()
#         # Process the data
#         print(data, "consumer")
#         break
#
#
# # Create the shared queue and launch both threads
# q = Queue()
# t1 = Thread(target=consumer, args=(q,))
# t2 = Thread(target=producer, args=(q, "fuck"))
# t1.start()
# t2.start()

import threading

import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._count = 0
        self._cv = threading.Condition()

    def put(self, item, priority):
        with self._cv:
            heapq.heappush(self._queue, (-priority, self._count, item))
            self._count += 1
            self._cv.notify()

    def get(self):
        with self._cv:
            while len(self._queue) == 0:
                self._cv.wait()
            return heapq.heappop(self._queue)[-1]
