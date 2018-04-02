#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author = 'wyx'
@time = 16/8/19 14:45
@annotation = '' 
"""


class A:
    def ping(self):
        print('A', self)


class B(A):
    def pong(self):
        print('B', self)


class C(A):
    def pong(self):
        print('C', self)


class D(B, C):
    def ping(self):
        super().ping()
        print('D', self)

    def pingpong(self):
        self.ping()
        super().ping()
        self.pong()
        super().pong()
        C.pong(self)


d = D()
# d.ping()

d.pingpong()
