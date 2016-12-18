#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author = 'wyx'
@time = 16/10/18 21:31
@annotation = '' 
"""
from functools import wraps


def log(func):
    @wraps(func)  # 这个函数的重要的元信息比如名字、文档字符串、注解和参数签名都丢失了。
    def wrapper(*args, **kwargs):
        print("Call before %s" % func.__name__)
        result = func(*args, **kwargs)
        print("Call after")
        return result

    return wrapper


def strong_log(desc):
    def new_deco(old_handler):
        @wraps(old_handler)
        def new_handler(*args, **kwargs):
            print("Call before")
            result = old_handler(*args, **kwargs)
            print("Call %s" % desc)
            return result

        return new_handler

    return new_deco


@strong_log("jlllll")
def test():
    print("Try")

    return "Hello"


if __name__ == '__main__':
    test()
    print(test.__name__)
