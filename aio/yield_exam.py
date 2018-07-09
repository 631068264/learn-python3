#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author = 'wyx'
@time = 2018/7/4 10:50
@annotation = ''
"""
a = range(50)


def b():
    for i in a:
        yield i


def c():
    yield from a


if False:
    for i in b():
        print(i)

    for i in c():
        print(i)


def gen():
    def subgen():
        while True:
            x = yield
            yield x + 1

    yield from subgen()


def main():
    g = gen()
    next(g)  # 驱动生成器g开始执行到第一个 yield
    retval = g.send(1)  # 看似向生成器 gen() 发送数据
    print(retval)  # 返回2
    g.throw(StopIteration)  # 看似向gen()抛入异常


main()
