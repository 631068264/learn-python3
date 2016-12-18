#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author = 'wyx'
@time = 2016/12/7 11:15
@annotation = '' 
"""
from abc import ABCMeta, abstractmethod


class IStream(metaclass=ABCMeta):
    """
    抽象类的一个特点是它不能直接被实例化
    抽象类的目的就是让别的类继承它并实现特定的抽象方法
    在代码中检查某些类是否为特定类型，实现了特定接口
    """

    @abstractmethod
    def read(self, maxbytes=-1):
        pass

    @abstractmethod
    def write(self, data):
        pass


class Singleton(type):
    def __init__(cls, *args, **kwargs):
        super(Singleton, cls).__init__(*args, **kwargs)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instance


class ValidMeta(type):
    def __new__(cls, name, *args, **kwargs):
        return type.__new__(cls, name, *args, **kwargs)


class Single(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(Single, cls).__new__(cls, *args, **kwargs)
        return cls._instance


class Myclass(object, metaclass=ValidMeta):
    def __init__(self, weight):
        self.weight = weight
        # weight = None


m = Myclass(-100)
print(m.weight)


class MetaTable(type):
    def __getattr__(cls, key):
        temp = key.split("__")
        name = temp[0]
        alias = temp[1] if len(temp) > 1 else None

        return cls(name, alias)


class Table(object, metaclass=MetaTable):
    def __init__(self, name, alias=None):
        self._name = name
        self._alias = alias


Table.table__t
