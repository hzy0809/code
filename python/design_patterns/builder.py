#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Hzy
# @file: builder.py
# @time: 2023/2/16 21:56

"""
https://www.liaoxuefeng.com/wiki/1252599548343744/1281319155793953
将一个复杂对象的构建与它的表示分离，使得同样的构建过程可以创建不同的表示
一般来说，是因为创建这个对象的步骤比较多，每个步骤都需要一个零部件，最终组合成一个完整的对象。
Builder模式是为了创建一个复杂的对象，需要多个步骤完成创建，或者需要多个零件组装的场景，且创建过程中可以灵活调用不同的步骤或组件。
"""


class UrlBuilder(object):
    def __init__(self):
        self.url = None
        self.params = {}
        self.format = []

    def set_domain(self, domain):
        self.params["domain"] = domain
        self.format.append((1, "{domain}"))
        return self

    def set_schema(self, schema):
        self.params["schema"] = schema
        self.format.append((0, "{schema}://"))
        return self

    def set_path(self, path):
        self.params["path"] = path
        self.format.append((2, "{path}"))
        return self

    def set_query(self, queries: dict):
        query = "&".join(f"{k}={v}" for k, v in queries.items())
        if query:
            self.params["query"] = query
            self.format.append((3, "?{query}"))
        return self

    def build(self):
        self.format.sort()
        self.url = "".join(f[1] for f in self.format).format(**self.params)
        return self


def main():
    builder = UrlBuilder().set_path("/home").set_schema("http").build()
    print(builder.url)


if __name__ == '__main__':
    main()
