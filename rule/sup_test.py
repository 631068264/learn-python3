#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author = 'wyx'
@time = 2016/12/30 11:03
@annotation = '' 
"""


class A:
    def __init__(self):
        self.n = 2

    def add(self, m):
        print('self is {0} @A.add'.format(self))
        self.n += m


class B(A):
    def __init__(self):
        self.n = 3

    def add(self, m):
        print('self is {0} @B.add'.format(self))
        # 确实调用了父类 A 的 add 方法 此时父类中 self 并不是父类的实例而是子类的实例
        super().add(m)
        self.n += 3


# b = B()
# b.add(2)
# print(b.n)
class C(A):
    def __init__(self):
        self.n = 4

    def add(self, m):
        print('self is {0} @C.add'.format(self))
        super().add(m)
        self.n += 4


class D(B, C):
    def __init__(self):
        self.n = 5

    def add(self, m):
        print('self is {0} @D.add'.format(self))
        super().add(m)
        self.n += 5
# D 的 MRO 是: [D, B, C, A, object]
# MRO 由左往右依次层次遍历
d = D()
d.add(2)
print(d.n)
