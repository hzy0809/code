#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Hzy
# @file: const.py
# @time: 2023/2/22 23:37
"""
项目常量
"""
from pathlib import Path

ProjectPath = Path(__file__).absolute().parent

if __name__ == '__main__':
    print(ProjectPath)