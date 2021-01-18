#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from redis import Redis

r = Redis(host='localhost', port=6379, db=0, decode_responses=True)
r.set('foo', 'bar')
print(r.get('foo'))
