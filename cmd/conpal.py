#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author = 'wyx'
@time = 2016/12/16 15:37
@annotation = '' 
"""
from concurrent.futures import ThreadPoolExecutor
from time import time

"""
并行(concurrency)
    PC does many different things seeming at the same time(One CPU)
并发(paralleism)
    Actually many different things seeming at the same time(One CPU)

Cpython 执行Python程序分两步
parse and compile the 源码 into bytecode
run bytecode with a stack-based interpreter

全局线程锁(GIL) global interpreter lock
互斥锁 防止CPython被多线程抢占 确保所有的bytecode interpreter with (Cpython C扩展)正常运行

GIL副作用
Java or C++ 的多线程程序可以充分利用多核
多线程IO密集型 计算密集型依赖CPU
Python虽然支持多线程,但是进行并行计算,加快程序就别指望了.

GIL不是万能的 不能避免数据抢夺
虽然在一个时刻内只有一个线程执行 Python解析器一个线程在数据结构上面的操作会被任意两个二进制指令之间打断

Python解析器让所有的线程保持一个平衡,让它们尽量获取相同的执行时间,
所以会挂起让另一个线程让另一个线程执行(不知道什么时候会挂起)

c.a += offset

value = getattr(c,"a")
result = value = offset
setattr(c,"a",result)


线程缺点
需要一些特殊的协调工作使得它们之间正常运行 使得程序变得复杂
线程消耗很多内存 大概8M一个 协程1K左右(协程也只是实现千万级别的并行)
线程的启动也消耗很大 一个新线程启动 正在运行的线程开销会变大同时会使得执行效率下降
"""


def simple_cor():
    def cor():
        """
        send a value back to the generator function
        after each yield expression

        send的值作为yield的结果返回

        yield 暂停 send from the outside 重新开始
        :return:
        """
        while True:
            received = yield
            print("Received:", received)

    it = cor()
    # 为generator接收第一个send做准备 把值推到第一个yield
    next(it)
    it.send("First")
    it.send("Second")


def mini():
    def minimize():
        current = yield
        while True:
            value = yield current
            current = min(value, current)

    it = minimize()
    next(it)
    print(it.send(10))
    print(it.send(4))
    print(it.send(22))
    print(it.send(-1))


def test():
    def te(x):
        yield x
        yield x + 1
        yield x + 2
        return 2

    def py2():
        # print(list(te(4)))
        for t in te(4):  # yield from in Python2
            yield t

    # py2()

    # print(list(py2()))

    # it = t(4)
    # q1 = next(it)
    # print(q1)
    # q2 = it.send(0)
    # print(q2)
    # q3 = it.send(-1)
    # print(q3)
    # try:
    #     q4 = it.send(-1)
    #     print(q4)
    # except StopIteration as e:
    #     print(e.value)
    def s(x):
        state = yield x
        d = yield from te(x)
        re = yield a(state, d)
        return re

    def d(x):
        it = s(x)
        p = next(it)
        print(p)
        p1 = it.send(0)
        print(p1)
        p2 = it.send(0)
        print(p2)

    def b(x):
        d = yield from te(x)
        return d

    def a(state, x):
        if x == 4:
            return x
        elif x == 0:
            return x
        elif x == 1:
            return x
        elif x == 2:
            return x

    def c(x):
        it = b(x)
        q1 = next(it)
        print(q1)
        q2 = it.send(0)
        print(q2)
        q3 = it.send(-1)
        print(q3)
        try:
            q4 = it.send(-1)
            print(q4)
        except StopIteration as e:
            print(e.value)


"""
实现真正的并发 child process
"""
numbers = [(1963309, 2265973), (2030677, 3814172), (1551645, 2229620), (2039045, 2020802)]


def gcd(pair):
    a, b = pair
    low = min(a, b)
    for i in range(low, 0, -1):
        if a % i == 0 and b % i == 0:
            return i


def normal():
    start = time()
    results = list(map(gcd, numbers))
    end = time()
    print("%.3f seconds" % (end - start,))


# normal()

def thpa():
    start = time()
    pool = ThreadPoolExecutor(max_workers=2)
    """
    ThreadPoolExecutor thread start & 交互需要时间

    ProcessPoolExecutor 适用于
    程序部分之间不用share state
    很少的数据 在主程序和子程序s之间pass 子程序s进行大量计算
    """
    # pool = ProcessPoolExecutor(max_workers=2)
    results = list(pool.map(gcd, numbers))
    end = time()
    print("%.3f seconds" % (end - start,))

# thpa()
