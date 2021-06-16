#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/15 17:32
# @Author  : hzy
# @File    : contextManager.py
# @Software: PyCharm

class Manager(object):
    pass


class Context(object):
    def __init__(self):
        self.manager = Manager()

    def __enter__(self):
        return self.manager

    def __exit__(self, exc_type, exc_value, exc_tb):
        if exc_type is None:
            print('no error')
        else:
            print('raise error')
            return False


if __name__ == '__main__':
    with Context() as c:
        print(1/0)
