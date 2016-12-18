#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author = 'wyx'
@time = 16/7/21 16:26
@annotation = '' 
"""
import asyncio

# @asyncio.coroutine
# def slow_operation(future):
#     yield from asyncio.sleep(1)
#     future.set_result('Future is done!')
#
#
# loop = asyncio.get_event_loop()
# future = asyncio.Future()
# asyncio.ensure_future(slow_operation(future))
# loop.run_until_complete(future)
# print(future.result())
# loop.close()

"""
非异步调用异步方法的结果
"""

l = []


@asyncio.coroutine
def slow_operation(future):
    yield from asyncio.sleep(1)
    future.set_result('Future is done!')


def got_result(future):
    print(future.result())
    l.append(future.result())
    loop.stop()


loop = asyncio.get_event_loop()
future = asyncio.Future()
asyncio.ensure_future(slow_operation(future))
future.add_done_callback(got_result)

try:
    loop.run_forever()
finally:
    print(l)
    loop.close()
