#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author = 'wyx'
@time = 16/7/18 17:13
@annotation = '' 
"""
import datetime
import asyncio


async def hello_world():
    print("Hello World!")


loop = asyncio.get_event_loop()
# Blocking call which returns when the hello_world() coroutine is done
loop.run_until_complete(hello_world())
loop.close()


# async def display_date(loop):
#     end_time = loop.time() + 5.0
#     while True:
#         print(datetime.datetime.now())
#         if (loop.time() + 1.0) >= end_time:
#             break
#         await asyncio.sleep(1)
#
#
# loop = asyncio.get_event_loop()
# # Blocking call which returns when the display_date() coroutine is done
# loop.run_until_complete(display_date(loop))
# loop.close()


async def compute(x, y):
    print("Compute %s + %s ..." % (x, y))
    await asyncio.sleep(1.0)
    return x + y

async def print_sum(x, y):
    result = await compute(x, y)
    print("%s + %s = %s" % (x, y, result))

loop = asyncio.get_event_loop()
loop.run_until_complete(print_sum(1, 2))
loop.close()