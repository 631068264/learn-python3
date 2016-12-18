#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author = 'wyx'
@time = 16/7/18 19:11
@annotation = '' 
"""
import asyncio
import datetime


# def hello_world(loop):
#     print('Hello World')
#     loop.stop()
#
#
# loop = asyncio.get_event_loop()
#
# # Schedule a call to hello_world()
# loop.call_soon(hello_world, loop)
#
# # Blocking call interrupted by loop.stop()
# loop.run_forever()
# loop.close()


def display_date(end_time, loop):
    print(datetime.datetime.now())
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, display_date, end_time, loop)
    else:
        loop.stop()


loop = asyncio.get_event_loop()

# Schedule the first call to display_date()
end_time = loop.time() + 5.0
loop.call_soon(display_date, end_time, loop)

# Blocking call interrupted by loop.stop()
loop.run_forever()
loop.close()
