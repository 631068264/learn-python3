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


def bar(future):
    print(future.result())
    return 'bar'


future = foo()
task = asyncio.ensure_future(future)
task.add_done_callback(bar)
loop = asyncio.get_event_loop()
# tasks = [foo(), bar()]
loop.run_until_complete(task)
loop.close()
# asyncio.run(task)
