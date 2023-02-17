#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Hzy
# @file: singleton.py
# @time: 2023/2/17 21:13
"""
保证一个类仅有一个实例，并提供一个访问它的全局访问点。
单例模式（Singleton）的目的是为了保证在一个进程中，某个类有且仅有一个实例。
Singleton模式是为了保证一个程序的运行期间，某个类有且只有一个全局唯一实例；
Singleton模式既可以严格实现，也可以以约定的方式把普通类视作单例。
"""


class Singleton(type):
    def __init__(cls, *args, **kwargs):
        cls.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance


class Spam(metaclass=Singleton):
    def __init__(self):
        print("Creating Spam")


class Item(object):
    __instance = None

    def __init__(self):
        print("Creating Item")

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = Item()
        return cls.__instance


def main():
    a = Spam()
    b = Spam()
    print(a is b)
    c = Item.get_instance()
    d = Item.get_instance()
    print(c is d)


if __name__ == '__main__':
    main()
