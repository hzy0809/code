#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   heap.py
@Time    :   2023/1/18 13:40 
@Author  :   zhenyu.hu
@Desc    :   <awaiting description>
"""

import heapq


def main():
    a = [1, 2, 2, 6, 4, 5, 3]
    heapq.heapify(a)
    heapq.heappop(a)


if __name__ == '__main__':
    main()
