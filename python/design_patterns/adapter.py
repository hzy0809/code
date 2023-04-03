#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Hzy
# @file: adapter.py
# @time: 2023/4/3 23:08
"""
将一个类的接口转换成客户希望的另外一个接口，使得原本由于接口不兼容而不能一起工作的那些类可以一起工作。
"""


class B(object):
    def exec(self, number=1):
        return number


class A(object):
    def run(self):
        return B().exec(10)
