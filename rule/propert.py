#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author = 'wyx'
@time = 2016/12/16 10:23
@annotation = '' 
"""
from weakref import WeakKeyDictionary


class Grade(object):
    def __init__(self):
        # 防止 Grade实例 被所有的Exam实例共享同一个属性
        # Grade实例只初始化一次 当Exam第一次定义的时候 并不是每次Exam实例化的时候
        self._values = WeakKeyDictionary()

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self._values.get(instance, 0)

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError("Grade 100")
        self._values[instance] = value


class Exam(object):
    math = Grade()
    science = Grade()

    # @property
    # def grade(self):
    #     return self._grade

    # @Grade
    # def grade(self, grade):
    #     # if not (0 <= grade <= 100):
    #     #     raise ValueError("Grade 100")
    #     # self._grade = grade
    #     return grade


h = Exam()
print(h.science, h.math)
h.science = 99
h.math = 100
print(h.science, h.math)
a = Exam()
a.science = 100
print(a.science, h.science)
