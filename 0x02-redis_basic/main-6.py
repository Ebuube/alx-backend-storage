#!/usr/bin/env python3
"""Test web cache"""
import redis
from time import sleep

get_page = __import__('web').get_page

url = 'http://slowwly.robertomurray.co.uk'
db = redis.Redis()


for count in range(0, 3):
    get_page(url)

print("Checking availability")
for count in range(0, 3):
    sleep(3)
    result = db.get(f'output:{url}')
    if result:
        result = result.decode('utf-8')
    calls = db.get(f'count:{url}')
    if calls:
        calls = calls.decode('utf-8')
    print("{}: {} : {}".format(url, calls, result[:5]))



# Accessing again
print("Accessing url again")
for count in range(0, 3):
    get_page(url)

print("Checking availability")
for count in range(0, 3):
    sleep(3)
    result = db.get(f'output:{url}')
    if result:
        result = result.decode('utf-8')
    calls = db.get(f'count:{url}')
    if calls:
        calls = calls.decode('utf-8')
    if result:
        print("{}: {} : {}".format(url, calls, result[:5]))
    else:
        print("{}: {} : {}".format(url, calls, result))
