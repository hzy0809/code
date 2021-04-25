#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from elasticsearch import Elasticsearch
from datetime import datetime

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
doc = {
    'author': 'kimchy',
    'text': 'Elasticsearch: cool. bonsai cool.',
    'timestamp': datetime.now(),
}

# index:类似于数据库
# doc_type:类似于表
# id:类似于索引
res = es.index(index='test-index', doc_type='tests', id=1, body=doc)
print(res['result'])

res = es.get(index='test-index', doc_type='tests', id=1)
print(res['_source'])
