#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author = 'wyx'
@time = 2016/12/7 17:46
@annotation = '' 
"""
import time

"""
Event
"""
import threading


# Code to execute in an independent thread
def countdown(n, started_evt):
    """
    Event 对象包含一个可由线程设置的信号标志，它允许线程等待某些事件的发生。

    在初始情况下，event 对象中的信号标志被设置为假。
    如果有线程等待一个 event 对象，而这个 event 对象的标志为假，那么这个线程将会被一直阻塞直至该标志为真。
    一个线程如果将一个 event 对象的信号标志设置为真，它将唤醒所有等待这个 event 对象的线程
    如果一个线程等待一个已经被设置为真的 event 对象，那么它将忽略这个事件，继续执行。

    Event.set() notify_all
    Event.wait() wait

    :param n:
    :param started_evt:
    :return:
    """
    print('countdown starting')
    started_evt.set()
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(5)


# Create the event object that will be used to signal startup
started_evt = threading.Event()

# Launch the thread and pass the startup event
print('Launching countdown')
t = threading.Thread(target=countdown, args=(10, started_evt))
t.start()

# Wait for the thread to start
started_evt.wait()
# started_evt 事件执行后才继续执行
print('countdown is running')


# class PeriodicTimer:
#     def __init__(self, interval):
#         self._interval = interval
#         self._flag = 0
#         self._cv = threading.Condition()
#
#     def start(self):
#         t = threading.Thread(target=self.run)
#         t.daemon = True
#
#         t.start()
#
#     def run(self):
#         '''
#         Run the timer and notify waiting threads after each interval
#         '''
#         while True:
#             time.sleep(self._interval)
#             with self._cv:
#                 self._flag ^= 1
#                 print(self._flag, "run")
#                 self._cv.notify_all()
#
#     def wait_for_tick(self):
#         '''
#         Wait for the next tick of the timer
#         '''
#         with self._cv:
#             last_flag = self._flag
#             print(self._flag, "wait_for_tick")
#             while last_flag == self._flag:
#                 print(self._flag, "_flag")
#                 self._cv.wait()
#
#
# # Example use of the timer
# ptimer = PeriodicTimer(5)
# ptimer.start()
#
#
# # Two threads that synchronize on the timer
# def countdown(nticks):
#     while nticks > 0:
#         ptimer.wait_for_tick()
#         print('T-minus', nticks)
#         nticks -= 1
#
#
# def countup(last):
#     n = 0
#     while n < last:
#         ptimer.wait_for_tick()
#         print('Counting', n)
#         n += 1
#
#
# threading.Thread(target=countdown, args=(6,)).start()
# threading.Thread(target=countup, args=(3,)).start()


# def worker(n, sema):
#     # Wait to be signaled
#     sema.acquire()
#
#     # Do some work
#     time.sleep(n)
#     print('Working', n)
#     sema.release()
#
#
# # Create some threads
# sema = threading.Semaphore(5)
# nworkers = 10
# for n in range(nworkers):
#     t = threading.Thread(target=worker, args=(n, sema,))
#     t.start()
