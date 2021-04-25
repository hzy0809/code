#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/2/27 22:05
# @Author  : hzy
# @File    : 00_gevent.py
# @Software: PyCharm

from gevent import monkey

monkey.patch_all()
from gevent import pool
import gevent
import time


def test(a, b):
    print('%s start' % gevent.getcurrent())
    time.sleep(b)
    print(a)
    return a


po = pool.Pool(10)
gevent.joinall([po.spawn(test, x, 1) for x in range(100)])

po = pool.Pool(10)
result = po.imap(test, map(lambda x: (x, 1), range(100)))
for i in result:
    print(i)
