#!/usr/bin/env python3
"""Writing strings to Redis"""
import redis
import uuid
from typing import Union, Callable, Any
from functools import wraps


def count_calls(f: Callable) -> Callable:
    """
    Track how many times a method of a class is called
    """
    @wraps(f)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        """
        Increment the number of calls
        Initialize to 1 if it is first call
        """
        self = args[0]
        self._redis.incr(f.__qualname__, 1)
        # Done increment
        return f(*args, **kwargs)
    return wrapper


class Cache:
    """
    Redis Cache
    """
    def __init__(self):
        """Initialize an instance"""
        self._redis = redis.Redis()
        # Delete everything stored in this database
        self._redis.flushdb()

    @count_calls
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
