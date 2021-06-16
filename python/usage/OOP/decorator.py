#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/15 15:56
# @Author  : hzy
# @File    : decorator.py
# @Software: PyCharm

"""
装饰器
"""


class Tracer(object):

    def __init__(self, func):
        self.func = func
        self.calls = 0

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print(f'calls {self.calls} to {self.func.__name__}')
        return self.func(*args, **kwargs)


@Tracer
def show_data(a):
    print(a)


def main():
    show_data(1)
    show_data(2)


if __name__ == '__main__':
    main()
