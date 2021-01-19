#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class ThirdClass(object):
    def __init__(self, value):
        """
        初始化实例属性
        :param value:
        """
        self.value = value

    def __add__(self, other):
        """
        python 将+左侧的实例对象传递个self参数，而将右侧的值传递给other
        :param other:
        :return:
        """
        return ThirdClass(self.value + other)

    # todo:__radd__优先级高于__add__?
    def __radd__(self, other):
        """
        与__add__类似，右侧的实例对象传递给self
        :param other:
        :return:
        """
        return ThirdClass(self.value + other)


if __name__ == '__main__':
    a = ThirdClass('abc')
    b = 'xzy' + a   # 如果为定义__radd__将引发TypeError
    print(b.value)
    # 类属性字典__dict__
    print(ThirdClass.__dict__.keys())
    # 超类元组
    print(ThirdClass.__bases__)
