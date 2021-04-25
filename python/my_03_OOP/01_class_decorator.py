#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
    """类内修饰器和__slots__"""

    # 限定实例属性，子类不继承
    # __slots__ would disable __dict__
    __slots__ = ('_name', '_age')

    def __init__(self, name, age: int = 18):
        self._name = name
        self._age = age

    # 添加类属性
    # 仅使用@property时，该属性为只读属性
    @property
    def name(self):
        return self._name

    # 类属性设置函数
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError('name must be str')
        if len(value) > 10:
            raise ValueError('name too long (>10)')
        self._name = value

    # @name.getter
    # def name(self):
    #     return self._name

    @staticmethod
    def test_static():
        pass

    @classmethod
    def test_class(cls):
        pass


if __name__ == '__main__':
    s = Student('a')
    # print(s.__dict__.keys())  #  AttributeError: 'Student' object has no attribute '__dict__'
    print(s.name)
    # s.name = 1  #  ValueError: name must be str
    print(Student.__dict__.keys())
