#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   decorator.py
@Time    :   2023/4/19 09:45 
@Author  :   zhenyu.hu
@Desc    :   <awaiting description>
"""
import logging
import time
from functools import wraps

"""
https://www.liaoxuefeng.com/wiki/1252599548343744/1281319302594594
动态地给一个对象添加一些额外的职责。就增加功能来说，相比生成子类更为灵活。
"""
logger = logging.getLogger(__name__)


def time_this(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        logger.info(f'{func.__qualname__} cost {end - start}')
        return result

    return wrapper


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)


    @time_this
    def countdown(n):
        while n > 0:
            n -= 1

    countdown(10000)
    countdown(10000000)
