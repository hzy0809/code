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
logger = logging.getLogger(__name__)
formatter = logging.Formatter("%(asctime)s;%(levelname)s;%(message)s")
ch = logging.StreamHandler()
ch.setFormatter(formatter)
logger.addHandler(ch)
logger.setLevel(level=logging.INFO)
