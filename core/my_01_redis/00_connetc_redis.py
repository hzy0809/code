#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from redis import Redis


def connect_redis():
    # host: IP地址，port：端口，db:默认数据库
    # decode_responses:自动编码，如果为False，默认返回bite类型
    r = Redis(host='localhost', port=6379, db=0, decode_responses=True)
    r.set('foo', 'bar')
    print(r.get('foo'))


if __name__ == '__main__':
    connect_redis()
