#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author = 'wyx'
@time = 2016/12/7 11:40
@annotation = '' 
"""


# class Proxy:
#     def __init__(self, obj):
#         self._obj = obj
#
#     # Delegate attribute lookup to internal obj
#     def __getattr__(self, name):
#         print('getattr:', name)
#         return getattr(self._obj, name)
#
#     # Delegate attribute assignment
#     def __setattr__(self, name, value):
#         if name.startswith('_'):
#             super().__setattr__(name, value)
#         else:
#             print('setattr:', name, value)
#             setattr(self._obj, name, value)
#
#     # Delegate attribute deletion
#     def __delattr__(self, name):
#         if name.startswith('_'):
#             super().__delattr__(name)
#         else:
#             print('delattr:', name)
#             delattr(self._obj, name)
#
#
# class Spam:
#     def __init__(self, x):
#         self.x = x
#
#     def bar(self, y):
#         print('Spam.bar:', self.x, y)


# s = Spam(2)
# p = Proxy(s)
# print(p.x)
# p.bar(3)
# p.x = 37
# print(p.x)


class Single(object):
    def __new__(cls, *args, **kwargs):
        """
        cls 是实例本身 其他参数pass到构造器
        :param args:
        :param kwargs:
        :return: 新的实例 返回cls 才执行 __init__
        """
        if not hasattr(cls, "_instance"):
            # create a new instance of the class
            cls._instance = super(Single, cls).__new__(cls, *args, **kwargs)
        return cls._instance


class Singleton(type):
    def __init__(cls, *args, **kwargs):
        cls.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)
            return cls.__instance
        else:
            return cls.__instance


class MyClass(metaclass=Singleton):
    # def __new__(cls, *args, **kwargs):
    #     print("new")

    # __metaclass__ = Singleton
    def __init__(self):
        print("init")
        self.page = ""


m = MyClass()
n = MyClass()
print(m == n)


# class LoggedMappingMixin:
#     """
#     Add logging to get/set/delete operations for debugging.
#     """
#     __slots__ = ()  # 混入类都没有实例变量，因为直接实例化混入类没有任何意义
#
#     def __getitem__(self, key):
#         print('Getting ' + str(key))
#         return super().__getitem__(key)
#
#     def __setitem__(self, key, value):
#         print('Setting {} = {!r}'.format(key, value))
#         return super().__setitem__(key, value)
#
#     def __delitem__(self, key):
#         print('Deleting ' + str(key))
#         return super().__delitem__(key)
#
#
# def LoggedMapping(cls):
#     """第二种方式：使用类装饰器"""
#     cls_getitem = cls.__getitem__
#     cls_setitem = cls.__setitem__
#     cls_delitem = cls.__delitem__
#
#     def __getitem__(self, key):
#         print('Getting ' + str(key))
#         return cls_getitem(self, key)
#
#     def __setitem__(self, key, value):
#         print('Setting {} = {!r}'.format(key, value))
#         return cls_setitem(self, key, value)
#
#     def __delitem__(self, key):
#         print('Deleting ' + str(key))
#         return cls_delitem(self, key)
#
#     cls.__getitem__ = __getitem__
#     cls.__setitem__ = __setitem__
#     cls.__delitem__ = __delitem__
#     return cls
#
#
# class LoggedDict(LoggedMappingMixin, dict):
#     pass
#
#
# d = LoggedDict()
# d['x'] = 23
# print(d['x'])
# del d['x']
