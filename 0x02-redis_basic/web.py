#!/usr/bin/env python3
"""Implementing an expiring web cache and tracker"""
import redis
import requests
from functools import wraps
from typing import Callable


# Make connection to Redis server
db = redis.Redis()
db.flushdb()


def cache(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(url: str) -> str:
        time_live = 10
        url_key = "count:{}".format(url)
        result_key = "output:{}".format(url)

        if not db.get(url_key):
            result = method(url)
            db.setex(url_key, time_live, 1)
            db.setex(result_key, time_live, result)
        else:
            db.incr(url_key)
            result_bytes = db.get(result_key)
            if result_bytes:
                result = result_bytes.decode('utf-8')

        return result
    return wrapper


@cache
def get_page(url: str) -> str:
    """
    Track the number of times a particular url was accessed
    Each cache lasts for only 10 seconds
    """
    return requests.get(url).text
