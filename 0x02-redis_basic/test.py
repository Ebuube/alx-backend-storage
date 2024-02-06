#!/usr/bin/env python3
"""Learning redis and Python"""
import redis

r = redis.Redis(decode_responses=True)
r.set('mykey', 'thevalueofmykey')
a = r.get('mykey')
print(a)
