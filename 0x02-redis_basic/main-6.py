#!/usr/bin/env python3
"""Test web cache"""
import redis
from time import sleep

get_page = __import__('web').get_page

url = 'http://slowwly.robertomurray.co.uk'
db = redis.Redis()


for count in range(0, 5):
    get_page(url)

print("Checking availability")
for count in range(0, 5):
    sleep(4)
    print("{}: {}".format(url, db.get(f'count:{url}')))



# Accessing again
print("Accessing url again")
for count in range(0, 5):
    get_page(url)

print("Checking availability")
for count in range(0, 5):
    sleep(4)
    print("{}: {}".format(url, db.get(f'count:{url}')))
