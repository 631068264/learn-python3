#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author = 'wyx'
@time = 2016/12/8 12:28
@annotation = '' 
"""
import subprocess

# cmd = "ls"
# out_bytes = subprocess.check_output(cmd, shell=True)
# out_text = out_bytes.decode('utf-8')
# print(out_text)

# subprocess.Popen(shlex.split(cmd, posix=False), shell=True)


# try:
#     out_bytes = subprocess.check_output(cmd, stderr=sys.stdout, shell=True)
# except subprocess.CalledProcessError as e:
#     out_bytes = e.output  # Output generated before error
#     code = e.returncode  # Return code
#     print(out_bytes.decode('utf-8'), code)


# Some text to send
# text = b'''
# hello world
# this is a test
# goodbye
# '''
#
# # Launch a command with pipes
# p = subprocess.Popen(['wc'],
#                      stdout=subprocess.PIPE,
#                      stdin=subprocess.PIPE)
#
# # Send the data and get the output
# stdout, stderr = p.communicate(text)
# print(stdout, stderr)
# # To interpret as text, decode
# out = stdout.decode('utf-8')
# err = stderr.decode('utf-8') if stderr else None
# print(out, err)
from time import time

import os


def sleep(second):
    cmd = "sleep %s"
    proc = subprocess.Popen(cmd % second, shell=True)
    return proc


def runsleep():
    start = time()
    procs = []
    for _ in range(10):
        procs.append(sleep(0.1))
    for p in procs:
        p.communicate()
    end = time()
    print(end - start)


def run_ssl():
    def ssl(data):
        env = os.environ.copy()
        env["password"] = b'\xe24U\n\xd0Q13S\x11'
        cmd = "openssl enc -des3 -pass env:password"
        # chains processes 好像unix的pipe一样把一个进程的output 放入stdin
        proc = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        proc.stdin.write(data)
        proc.stdin.flush()
        return proc

    procs = []
    for _ in range(3):
        data = os.urandom(10)
        procs.append(ssl(data))
    for p in procs:
        out, err = p.communicate()
        print(out[-10:])


def poll():
    cmd = "sleep 0.3"
    proc = subprocess.Popen(cmd, shell=True)
    while proc.poll() is None:
        print("Loading ...")
    print("Done %s " % proc.poll())


def timeout():
    proc = sleep(10)
    try:
        proc.communicate(timeout=0.1)
    except subprocess.TimeoutExpired:
        proc.terminate()
        proc.wait()
    print("Done %s" % proc.poll())
