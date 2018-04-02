#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author = 'wyx'
@time = 2017/10/14 22:52
@annotation = ''
"""
import collections
from functools import wraps


def coroutine(func):
    """Decorator: primes `func` by advancing to first `yield`"""

    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen

    return primer


if False:
    def simple_coro2(a):
        print('-> Started: a =', a)
        b = yield a
        print('-> Received: b =', b)
        c = yield a + b
        print('-> Received: c =', c)


    cor = simple_coro2(13)
    next(cor)
    print(cor.send(1))
    print(cor.send(2))

if False:
    # @coroutine
    def avg():
        total = 0.0
        count = 0
        average = None
        while True:
            term = yield
            if term is None:
                break
            total += term
            count += 1
            average = total / count

        return count, average


    def common():
        coro_avg = avg()
        next(coro_avg)
        print(coro_avg.send(10))
        print(coro_avg.send(5))
        print(coro_avg.send(5))
        print(coro_avg.send(1))
        try:
            print(coro_avg.send(None))
        except StopIteration as e:
            print(e.value)
            # print(coro_avg.close())


    def new_method():
        values = [10, 5, 5, 1]
        coro_avg = avg()
        next(coro_avg)
        for v in values:
            coro_avg.send(v)
            r = yield from avg()
            print(r)


    common()
    # new_method()
if True:
    Event = collections.namedtuple('Event', 'time proc action')
    # class Event:
    #     def __init__(self, time, id, msg):
    #         self.time = time
    #         self.id = id
    #         self.msg = msg
    #
    #     def __repr__(self):
    #         return '%s(%s)' % (self.__class__.__name__, self.__dict__)


    def taxi_process(ident, trips, start_time=0):
        """Yield to simulator issuing event at each state change"""
        time = yield Event(start_time, ident, 'leave garage')
        for i in range(trips):
            time = yield Event(time, ident, 'pick up passenger')
            time = yield Event(time, ident, 'drop off passenger')
        yield Event(time, ident, 'going home')


    time = 0
    taxi = taxi_process(ident=13, trips=2, start_time=0)
    print(next(taxi))
    print(taxi.send(time + 7))
    print(taxi.send(time + 23))
    print(taxi.send(time + 5))
    print(taxi.send(time + 48))
    print(taxi.send(time + 1))
    print(taxi.send(time + 10))
