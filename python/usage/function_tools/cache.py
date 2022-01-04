#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/12/27 11:31
# @File    : cache.py
# @Software: PyCharm

from functools import lru_cache


#
@lru_cache(maxsize=2, typed=False)
def test(number: int):
    print('number')
    return number


if __name__ == '__main__':
    test(1)
    test(1)
    print(test.cache_info())
    test.cache_clear()
    test(1)
