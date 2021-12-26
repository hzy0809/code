#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: hzy
# @file: factory.py
# @time: 2021/12/26 15:59

"""
定义一个用于创建对象的接口，让子类决定实例化哪一个类。Factory Method使一个类的实例化延迟到其子类。
"""
from datetime import datetime


class Factory(object):
    def parse(self, value):
        pass

    @classmethod
    def get_factory(cls):
        return NumberFactory()


class NumberFactory(Factory):

    def parse(self, value):
        return int(value)


# 静态工厂
class LocalDateFactory(object):

    @staticmethod
    def format_int(value):
        return datetime.strptime(str(value), '%Y%m%d').date()


if __name__ == '__main__':
    number_factory = Factory.get_factory()
    result = number_factory.parse('123')
    LocalDateFactory.format_int(20200202)
