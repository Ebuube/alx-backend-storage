#!/usr/bin/env python3
"""Test web cache"""
import redis
from time import sleep

get_page = __import__('web').get_page

url = 'http://slowwly.robertomurray.co.uk'
db = redis.Redis()

get_page(url)

# Verifying content is cached
print("Verifying content is cached")
for count in range(0, 4):
    time_live = 3
    sleep(time_live)
    calls = db.get(f'count:{url}')
    result_bytes = db.get(f'output:{url}')
    if result_bytes:
        result = result_bytes.decode('utf-8')[0:5]
    else:
        result = result_bytes

    print(f"time: {time_live * count} : {result}")



get_page(url)
# Verify content is recached if None
print("Verify content is recached if None")
for count in range(0, 4):
    time_live = 3
    sleep(time_live)
    calls = db.get(f'count:{url}')
    result_bytes = db.get(f'output:{url}')
    if result_bytes:
        result = result_bytes.decode('utf-8')[0:5]
    else:
        result = result_bytes

    print(f"time: {time_live * count} : {result}")


