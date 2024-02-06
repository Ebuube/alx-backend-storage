#!/usr/bin/env python3
"""Implementing an expiring web cache and tracker"""
import redis
import requests
from functools import wraps
from typing import Callable


# Make connection to Redis server
db = redis.Redis()
# db.flushdb()


def cache(method: Callable) -> Callable:
    """
    Track the number of times a particular url was accessed
    Cache the result
    Each cache lasts for only 10 seconds
    """
    @wraps(method)
    def wrapper(url: str) -> str:
        """
        Execute logic
        """
        time_live = 10
        url_key = "count:{}".format(url)
        result_key = "output:{}".format(url)

        if not db.get(result_key):
            result = method(url)
            db.incr(url_key)
            db.setex(result_key, time_live, result)
        else:
            result_bytes = db.get(result_key)
            if result_bytes:
                result = result_bytes.decode('utf-8')
            else:
                result = result_bytes

        return result
    return wrapper


@cache
def get_page(url: str) -> str:
    """
    Fetch a page from url
    """
    return requests.get(url).text
