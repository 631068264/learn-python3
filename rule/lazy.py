#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author = 'wyx'
@time = 2016/12/7 09:55
@annotation = '' 
"""


class lazyproperty(object):
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            return value

    # def __getattr__(self, item):
    #     # 找不到该属性时调用 AttributeError:  object has no attribute
    #     # 找到了就不会进来
    #     print(item, "__getattr__")
    #
    # def __getattribute__(self, item):
    #     # 定义了__getattribute__ 就不会调用__getattr__
    #     # 除非直接在__getattribute__里面调用__getattr__ or raise AttributeError
    #     # print(item, "__getattribute__")
    #     if item not in self:
    #         raise AttributeError(item)
    #     pass


import math


class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    @lazyproperty
    def area(self):
        print('Computing area')
        return math.pi * self.radius ** 2

    @lazyproperty
    def perimeter(self):
        print('Computing perimeter')
        return 2 * math.pi * self.radius


c = Circle(4.0)

print(c.area)
print(c.area)
print(c.perimeter)
print(c.perimeter)

# l = lazyproperty(11)
# l.aear
