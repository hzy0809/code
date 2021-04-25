#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
所有的类都是type类的实例
metaclass是type类的派生类
"""

from collections import OrderedDict


# A set of descriptors for various types
class Typed:
    _expected_type = type(None)

    def __init__(self, name=None):
        self._name = name

    def __set__(self, instance, value):
        if not isinstance(value, self._expected_type):
            raise TypeError('Expected ' + str(self._expected_type))
        instance.__dict__[self._name] = value


class Integer(Typed):
    _expected_type = int


class Float(Typed):
    _expected_type = float


class String(Typed):
    _expected_type = str


# Metaclass that uses an OrderedDict for class body
class OrderedMeta(type):
    def __new__(mcs, cls_name, bases, cls_dict):
        """
        创建类时执行 class A(metaclass)
        :param cls_name: 类名
        :param bases: 父类元组
        :param cls_dict: 属性字典
        """
        d = dict(cls_dict)
        order = []
        for name, value in cls_dict.items():
            if isinstance(value, Typed):
                value._name = name
                order.append(name)
        d['_order'] = order
        return type.__new__(mcs, cls_name, bases, d)

    @classmethod
    def __prepare__(mcs, cls_name, bases):
        """
        返回存储类属性的字典
        :param cls_name:
        :param bases:
        :return:mapping
        """
        return OrderedDict()


class Structure(metaclass=OrderedMeta):
    def as_csv(self):
        return ','.join(str(getattr(self, name)) for name in self._order)


# Example use
class Stock(Structure):
    name = String()
    shares = Integer()
    price = Float()

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price


if __name__ == '__main__':
    s = Stock('name', 100, 10.1)
    print(s.as_csv())
    s = Stock(1, 1, 1)
