#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author = 'wyx'
@time = 2018/7/4 14:52
@annotation = ''
"""
import asyncio


async def URL(url, sec):
    # if url == 'bar':
    #     raise Exception('爱啦啦啦')
    import random
    await asyncio.sleep(random.randint(0, 2) * 0.001)
    # await asyncio.sleep(0)
    return url


async def foo():
    print('Running in foo')
    await asyncio.sleep(0)
    print('Explicit context switch to foo again')
    result = await URL('foo', 3)
    return result


async def bar():
    print('Explicit context to bar')
    await asyncio.sleep(0)
    print('Implicit context switch back to bar')
    result = await URL('bar', 5)
    return result


tasks = [bar(), foo()]


async def main():
    await asyncio.gather(*tasks)


async def get_url():
    for future in asyncio.as_completed(tasks):

        fut = await future
        print(fut)


asyncio.run(get_url())
# asyncio.run(main())