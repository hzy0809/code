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

    def __contains__(self, item):
        """
        in 通常实现为迭代
        __contains__优先于__iter__
        __iter__优先于__getitem__
        :param item:
        :return:
        """
        return item in self.data

    def __getattr__(self, item):
        """
        拦截未定义的属性或者实例的点号运算
        :param item:string, attr name
        :return:
        """
        pass

    def __getattribute__(self, item):
        """

        :param item:
        :return:
        """
        pass

    def __setattr__(self, key, value):
        """
        拦截所有属性的赋值语句
        :param key:
        :param value:
        :return:
        """
        self.__dict__[key] = value

    def __repr__(self):
        """
        适用于一切环境，优先级低于__str__
        :return:string
        """
        pass

    def __str__(self):
        """
        响应print和str
        :return:string
        """
        pass

    def __add__(self, other):
        """
        不支持+运算符右侧使用实例对象
        :param other:
        :return:
        """
        return self.data + other

    def __radd__(self, other):
        """
        只有当右侧使用实例对象，左侧不使用实例对象时调用
        :param other:
        :return:
        """
        return other + self.data

    def __iadd__(self, other):
        """
        原处修改，优先级高于__add__
        :param other:
        :return:
        """
        pass

    def __sub__(self, other):
        """
        捕捉减法表达式
        :param other:
        :return:
        """
        return Instance(self.data - other)

    def __call__(self, *args, **kwargs):
        """
        为实例应用函数表达式提供支持,实现函数回调，或者函数绑定
        装饰器
        :param args:
        :param kwargs:
        :return:
        """

    def __gt__(self, other):
        """
        __lt__,__eq__,__ne__等
        没有隐式关系，==并不意味!=是假
        :param other:
        :return:
        """
        return self.data > other

    def __bool__(self):
        """
        获取bool值优先使用__bool__，如果未定义，则使用__len__,如果__len__未定义，则返回True
        :return:
        """
        pass

    def __len__(self):
        """

        :return:
        """
        pass

    def __del__(self):
        """
        析构函数，对象回收
        :return:
        """
        pass


class Commuter(object):
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        if isinstance(other, Commuter):
            other = other.val
        return Commuter(self.val + other)

    def __radd__(self, other):
        return Commuter(other + self.val)

    def __gt__(self, other):
        return self.val > other



if __name__ == '__main__':
    c1 = Commuter(1)
    c2 = Commuter(2)
    c3 = c1 + c2
    # __add__不进行类型判断时，c3.val是一个Commuter对象
    print(c3.val)

    cb3 = (lambda color='red': 'turn ' + color)
    print(cb3('blue'))
