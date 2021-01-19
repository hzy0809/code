#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

# 修改工作目录
os.chdir('/Users/huzhenyu/Documents')

# 获取当前目录
os.getcwd()

# 判断目录是否存在
os.path.exists('test')

# 判断路径是否为文件
os.path.isfile('test')

# 获取目录下的路径列表
os.listdir('test')

# 修改文件名称
os.rename('test', 'test_1')
