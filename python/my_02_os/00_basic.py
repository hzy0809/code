#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

# 获取当前文件的绝对路径
# __file__宏
path = os.path.abspath(__file__)

# 修改工作目录
os.chdir('/Users/huzhenyu/Documents')

# 获取当前目录
os.getcwd()

# 判断目录是否存在
os.path.exists('test')

# 判断路径是否为文件
os.path.isfile('test')

# 判断路径是否为目录
os.path.isdir('test')

# 获取目录下的路径列表
os.listdir('test')

# 修改文件名称
os.rename('test', 'test_1')


path += '/test'
# 创建目录
os.mkdir(path)

# 递归创建目录
os.makedirs(path)

#