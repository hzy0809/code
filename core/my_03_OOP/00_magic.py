#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class SingleMetaClass(type):
    """
    单例模式
    """

    def __init__(cls, *args, **kwargs):
        cls.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        """

        :param args:
        :param kwargs:
        :return:
        """
        print('__call__')
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)
            return cls.__instance
        else:
            if args or kwargs:
                cls.__instance.__init__(*args, **kwargs)
            return cls.__instance


class ThirdClass(metaclass=SingleMetaClass):

    def __init__(self, value):
        """
        初始化实例属性
        :param value:
        """
        self.value = value
        self.name = None
        print('__init__')

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
    b = 'xyz' + a  # 如果为定义__radd__将引发TypeError
    print(b.value)
    c = ThirdClass()
    print(a is c)
    # 类属性字典__dict__
    print(ThirdClass.__dict__.keys())
    # 超类元组
    print(ThirdClass.__bases__)
