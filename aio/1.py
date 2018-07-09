#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author = 'wyx'
@time = 2018/7/4 14:52
@annotation = ''
"""
import asyncio


async def foo():
    print('Running in foo')
    await asyncio.sleep(0)
    print('Explicit context switch to foo again')
    return 'foo'


async def bar():
    print('Explicit context to bar')
    await asyncio.sleep(0)
    print('Implicit context switch back to bar')
    return 'bar'


async def main():
    tasks = [foo(), bar()]
    await asyncio.gather(*tasks)


# loop = asyncio.get_event_loop()
# tasks = [foo(), bar()]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()
asyncio.run(main())
