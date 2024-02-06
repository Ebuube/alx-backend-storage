#!/usr/bin/env python3
"""Implementing an expiring web cache and tracker"""
import redis
import requests


# Make connection to Redis server
db = redis.Redis()
db.flushdb()


def get_page(url: str) -> str:
    """
    Track the number of times a particular url was accessed
    Each cache lasts for only 10 seconds
    """
    time_live = 10
    url_key = "count:{}".format(url)
    if not db.get(url_key):
        db.setex(url_key, time_live, 1)
    else:
        db.incr(url_key, 1)
    result = requests.get(url)
    return result.text
