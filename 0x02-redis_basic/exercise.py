#!/usr/bin/env python3
"""Writing strings to Redis"""
import redis
import uuid
from typing import Union, Callable


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

    def get(self,
            key: str,
            fn: Callable = None) -> Union[str, bytes, int, float, None]:
        """Return a key from Redis server"""
        val = self._redis.get(key)
        if not val:
            return None

        if fn is None:
            return val

        return fn(val)

    def get_str(self, key: str) -> Union[str, bytes, int, float, None]:
        """Return a string value"""
        val = self._redis.get(key)
        if not val:
            return None

        return val.decode('utf-8')

    def get_int(self, key: str) -> Union[str, bytes, int, float, None]:
        """Return a integer value"""
        val = self._redis.get(key)
        if not val:
            return None

        return int(val)
