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


def tracer(fuc):
    calls = 0

    def decorator(*args, **kwargs):
        nonlocal calls
        calls += 1
        # print(calls)
        return fuc(*args, **kwargs)

    # print(id(decorator))

    return decorator


@Tracer
def show_data(a):
    print(a)


def main():
    show_data(1)
    show_data(2)
    a = Test(1, 2)
    print(a.age)
    b = Test(3, 4)
    print(b.age)
    print(a.age)
    print(a + 1)


def dct(cls):
    class OnDct(Tools):
        def __init__(self, *args, **kwargs):
            self.__wrapped = cls(*args, **kwargs)

        def __getattr__(self, item):
            return getattr(self.__wrapped, item)

        def __setattr__(self, key, value):
            if key == '_OnDct__wrapped':
                self.__dict__[key] = value
            else:
                setattr(self.__wrapped, key, value)

    return OnDct


class Tools:
    def __add__(self, other):
        return self.age + other


@dct
class Test(Tools):
    def __init__(self, name, age):
        self.name = name
        self.age = age


if __name__ == '__main__':
    main()
