#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author = 'wyx'
@time = 2016/12/3 12:15
@annotation = '' 
"""


# with open("sdf.log", "w", encoding="utf-8") as f:
#     f.write("adf收到sdfad按时发生法律")

# a = 4
# b = 9
# for i in range(2, min(a, b), 1):
#     print("Test ", i)
#     if a % i == 0 and b % i == 0:
#         print("Not coprime")
#         break
# else:
#     print("eles Bolock")


def ffsdf():
    try:
        print("try")
        assert 2 == 3

    except Exception as e:
        print(e)
    else:
        print("else")
    finally:
        print("fillnal")
        return "fillnal"


print(ffsdf())

# current = {"green": 12, "blue": 3}
# increments = [
#     ("red", 5),
#     ("blue", 17),
#     ("orange", 9),
# ]
#
#
# def log_missing():
#     print("Key added")
#     return 0
