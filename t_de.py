#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author = 'wyx'
@time = 2018/7/21 22:18
@annotation = ''
"""
# import decimal
#
# # context = decimal.getcontext()
# # precision = min(context.prec - 2, 3)
# # print(context.prec)
# d = decimal.Decimal('3.27522').quantize(decimal.Decimal('0.00'), rounding=decimal.ROUND_HALF_EVEN)
# print(d)
#
# a = decimal.Decimal('10') ** (-1)
# print(a)
#
# print(str('$656316.65204$44892zzz').strip("$z"))
import tesserocr
from PIL import Image

img = Image.open('code.jpeg')
img = img.convert('L')
img.show()
result = tesserocr.image_to_text(img)
print(result)
