#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Hzy
# @file: composite.py
# @time: 2023/4/9 14:04
"""
https://www.liaoxuefeng.com/wiki/1252599548343744/1281319283720226
将对象组合成树形结构以表示“部分-整体”的层次结构，使得用户对单个对象和组合对象的使用具有一致性。
"""
import abc


class Node(abc.ABC):

    def add(self, node):
        pass

    def to_xml(self):
        pass


class ElementNode(Node):

    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, node):
        self.children.append(node)
        return self

    def to_xml(self):
        start = f"<{self.name}>\n"
        end = f"</{self.name}>\n"
        return start + "".join(node.to_xml() for node in self.children) + end


class TextNode(Node):
    def __init__(self, text):
        self.text = text

    def add(self, node):
        raise NotImplemented

    def to_xml(self):
        return self.text


class CommentNode(Node):
    def __init__(self, text):
        self.text = text

    def add(self, node):
        raise NotImplemented

    def to_xml(self):
        return f"<!-- {self.text} -->"


def main():
    root = ElementNode("school")
    root.add(
        ElementNode("classA").add(TextNode("Tom")).add(TextNode("Alice"))
    ).add(
        ElementNode("classB").add(TextNode("Bob")).add(TextNode("Grace")).add(CommentNode("comment..."))
    )
    print(root.to_xml())


if __name__ == '__main__':
    main()
