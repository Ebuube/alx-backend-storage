#!/usr/bin/env python3
"""Writing strings to Redis"""
import redis
import uuid
from typing import Union


class Cache:
    """
    Redis Cache
    """
    def __init__(self):
        """Initialize an instance"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store the string using a random key"""
        accepted_types = [str, bytes, int, float]
        if type(data) not in accepted_types:
            return ''

        key = str(uuid.uuid4())
        self._redis.set(key, data)

        return key
