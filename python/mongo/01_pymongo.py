#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pymongo import MongoClient

# 实例化client,建立连接
client = MongoClient(host='127.0.0.1', port=27017)

# 获取指定集合
collection = client['test']['t251']

# 插入一条文档
ret1 = collection.insert_one({'name': 'wang', 'age': 10})
print(ret1.inserted_id)

# 插入多条文档
data_list = [{'name': 'test{}'.format(i)} for i in range(10)]
ret2 = collection.insert_many(data_list)
print(ret2.inserted_ids)

# 查询一个记录
t = collection.find({'name': 'wang'})
# t是一个cursor对象，是一个迭代器，可以转换成列表
for i in t:
    print(i)

# 更新
u = collection.update_one({'name': 'wang'}, {'$set': {'name': 'new_wang'}})
print(u.raw_result)
print(u.acknowledged)
print(u.matched_count)

u = collection.update_many({'name': 'wang'}, {'$set': {'name': 'new_li'}})
print(u.raw_result)
print(u.acknowledged)
print(u.matched_count)

# 删除
d = collection.delete_one({'name': 'new_wang'})
print(d.raw_result)
d = collection.delete_many({'name': 'new_wang'})
print(d.raw_result)

date_list = [{'_id': i, 'name': 'py{}'.format(i)} for i in range(1000)]
collection.insert_many(date_list)

# 练习
ret = collection.find({'name': {'$regex': r'^py'}})
date_list = list(i for i in ret if int(str(i['_id'])) % 100 == 0)
print(date_list)
