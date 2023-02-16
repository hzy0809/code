#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/3/9 11:07
# @File    : abstract_factory.py
# @Software: PyCharm

"""
https://www.liaoxuefeng.com/wiki/1252599548343744/1281319134822433
提供一个创建一系列相关或相互依赖对象的接口，而无需指定它们具体的类。
抽象工厂模式和工厂方法不太一样，它要解决的问题比较复杂，不但工厂是抽象的，产品是抽象的，而且有多个产品需要创建，
因此，这个抽象工厂会对应到多个实际工厂，每个实际工厂负责创建多个实际产品
"""

# 抽象工厂
import typing


# 抽象产品
class HtmlDocument(object):
    def __init__(self, md):
        ...

    def save(self, path):
        ...


class WordDocument(object):
    def __init__(self, md):
        ...

    def save(self, path):
        ...


class AbstractFactory(object):
    def create_html(self, md) -> HtmlDocument:
        ...

    def create_word(self, md) -> WordDocument:
        ...


# 实际产品
class FastHtmlDocument(HtmlDocument):
    def to_html(self):
        ...

    def save(self, path):
        ...


class FastWordDocument(WordDocument):
    def save(self, path):
        ...


# 实际工厂
class FastFactory(AbstractFactory):
    def create_html(self, md):
        return FastHtmlDocument(md)

    def create_word(self, md):
        return FastWordDocument(md)


# 通过替换具体的工厂实现具体的功能
def main(factory: typing.Type[AbstractFactory]):
    f = factory()
    html = f.create_html("md")
    html.save("path")
    word = f.create_word("md")
    word.save("path")


if __name__ == '__main__':
    main(FastFactory)
