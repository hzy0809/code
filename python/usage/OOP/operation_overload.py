#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/4/26 16:16
# @Author  : hzy
# @File    : operation_overload.py
# @Software: PyCharm

class Instance:
    def __init__(self, data):
        """
        拦截实例的构造函数
        """
        self.data = data

    def __sub__(self, other):
        """
        捕捉减法表达式
        :param other:
        :return:
        """
        return Instance(self.data - other)

    def __del__(self):
        """
        析构函数，对象回收
        :return:
        """
        pass

    def __getitem__(self, item):
        """
        索引x[i]、切片x[i:j]以及迭代（in，map，for，类型构造list等，列表解析，列表和元组的赋值运算）
        迭代的优先级在__iter__之后
        :param item:int or slice object
        :return:
        """
        return self.data[item]

    def __setitem__(self, key, value):
        """
        similar to __getitem__
        :param key:
        :param value:
        :return:
        """
        self.data[key] = value

    def __iter__(self):
        """

        :return:
        """
        return self

    def __next__(self):
        """

        :return:
        """
        pass
