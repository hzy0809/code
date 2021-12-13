#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/8/6 16:06
# @Author  : hzy
# @File    : logging_usage.py
# @Software: PyCharm

import logging

# 该语句对全局生效
# logging.basicConfig(level=logging.INFO, format="%(asctime)s;%(levelname)s;%(message)s")

# 下方语句对该module生效
"""
%(pathname)s Full pathname of the source file where the logging call was issued(if available).

%(filename)s Filename portion of pathname.

%(module)s Module (name portion of filename).

%(funcName)s Name of function containing the logging call.

%(lineno)d Source line number where the logging call was issued (if available).
"""
logger = logging.getLogger(__name__)
formatter = logging.Formatter("%(asctime)s;%(levelname)s;%(message)s")
ch = logging.StreamHandler()
ch.setFormatter(formatter)
logger.addHandler(ch)
logger.setLevel(level=logging.INFO)
