#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author = 'wyx'
@time = 2018/7/20 16:24
@annotation = ''
"""
asks = [(8, 88), (9, 90), (11, 88), (12, 70), (14, 20)]
bids = [(13, 200), (9, 90), (8, 88), (3, 70), (1, 20)]

"""
4 2
88 440 88 8 13
88 440.0 88 8 13.0
178 800.0 178 8.50561797752809 13
200 844.0000000000002 200 8.78 13
200 844.0000000000002 200 8.78 13
2 0
844.0000000000002 200 11 13 8.78 13
"""

# amount = 0
# b_p,b_a = bids[0]
# for a_p, a_a in asks:
#     if b_p > a_p:
#         if b_a > a_a:
#             amount += a_a
#             print(min(amount, b_a), b_p, a_p)

max_i = 0
while asks[max_i][0] < bids[0][0]:
    if max_i >= len(asks) - 1:
        break
    max_i += 1

max_j = 0
while asks[0][0] < bids[max_j][0]:
    if max_j >= len(bids) - 1:
        break
    max_j += 1
