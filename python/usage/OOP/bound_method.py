#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/12 11:11
# @Author  : hzy
# @File    : bound_method.py
# @Software: PyCharm

"""
绑定方法
"""


class KA(object):
    def __init__(self, data):
        self.data = data

    def run(self):
        print(self.data)


class KB(object):
    def __init__(self, data):
        self.data = data

    # def run(self):
    #     print(self.data)


if __name__ == '__main__':
    a = KA('a')
    b = KB('b')
    KA.run(b)
    a.run()
