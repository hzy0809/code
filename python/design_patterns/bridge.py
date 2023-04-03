#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Hzy
# @file: bridge.py
# @time: 2023/4/3 23:15
"""
https://www.liaoxuefeng.com/wiki/1252599548343744/1281319266943009
将抽象部分与它的实现部分分离，使它们都可以独立地变化。
"""
import typing
from functools import wraps

Empty = object()


class Backend(object):

    def __init__(self):
        self._items = {}

    def save(self, key, result):
        self._items[key] = result

    def get(self, key):
        return self._items.get(key, Empty)


class HYCache(object):

    def __init__(self, backend=None):
        self.backend = backend or Backend()

    def __call__(self, fn: typing.Callable, **options):
        key = fn.__qualname__

        @wraps(fn)
        def decorator(*args, **kwargs):
            result = self.backend.get((key, args))
            if result is Empty:
                result = fn(*args, **kwargs)
                self.backend.save((key, args), result)
            return result

        return decorator


@HYCache()
def add(a, b):
    return a + b


if __name__ == '__main__':
    print(add(1, 2))
    print(add(3, 4))
