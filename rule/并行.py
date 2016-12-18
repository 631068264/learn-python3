#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author = 'wyx'
@time = 2016/12/7 23:26
@annotation = '' 
"""
import glob
import gzip
from concurrent import futures

import io

"""
一个 ProcessPoolExecutor 创建N个独立的Python解释器， N是系统上面可用CPU的个数。
你可以通过提供可选参数给 ProcessPoolExecutor(N) 来修改 处理器数量。
这个处理池会一直运行到with块中最后一个语句执行完成， 然后处理池被关闭。
程序会一直等待直到所有提交的工作被处理完成。

有两种方法去提交。
pool.map()
pool.submit()

回调
def when_done(r):
    print('Got:', r.result())

with ProcessPoolExecutor() as pool:
     future_result = pool.submit(work, arg)
     future_result.add_done_callback(when_done)
"""


def find_robots(filename):
    '''
    Find all of the hosts that access robots.txt in a single log file

    '''
    robots = set()
    with gzip.open(filename) as f:
        for line in io.TextIOWrapper(f, encoding='ascii'):
            fields = line.split()
            if fields[6] == '/robots.txt':
                robots.add(fields[0])
    return robots


def find_all_robots(logdir):
    '''
    Find all hosts across and entire sequence of files
    '''
    files = glob.glob(logdir + '/*.log.gz')
    all_robots = set()
    with futures.ProcessPoolExecutor() as pool:
        for robots in pool.map(find_robots, files):
            all_robots.update(robots)
    return all_robots


if __name__ == '__main__':
    robots = find_all_robots('logs')
    for ipaddr in robots:
        print(ipaddr)
