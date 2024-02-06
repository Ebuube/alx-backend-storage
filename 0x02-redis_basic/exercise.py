#!/usr/bin/env python3
"""Writing strings to Redis"""
import redis
import uuid
from typing import Union, Callable, Any
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Track how many times a method of a class is called
    """
    @wraps(method)
    def wrapper(self, *args: Any, **kwargs: Any) -> Any:
        """
        Increment the number of calls
        Initialize to 1 if it is first call
        """
        self._redis.incr(method.__qualname__, 1)
        # Done increment
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Track inputs and outputs of the function called
    """
    @wraps(method)
    def wrapper(self, *args: Any, **kwargs: Any) -> Any:
        """
        Append arguments and outputs
        Note:
        Ignore kwargs
        """
        inputs = method.__qualname__ + ':inputs'
        outputs = method.__qualname__ + ':outputs'

        for arg in args:
            self._redis.rpush(inputs, str(args))

        result = method(self, *args, **kwargs)
        self._redis.rpush(outputs, str(result))
        return result
    return wrapper


def replay(method: Callable) -> None:
    """
    Display the history of calls of a particular function
    """
    db = redis.Redis()
    name = method.__qualname__
    num_calls_bytes = db.get(name)
    if num_calls_bytes is None:
        num_calls = 0
    else:
        num_calls = int(num_calls_bytes.decode('utf-8'))

    inputs = db.lrange("{}:inputs".format(name), 0, -1)
    outputs = db.lrange("{}:outputs".format(name), 0, -1)
    print("{} was called {} times:".format(name, num_calls))
    for step in range(0, num_calls):
        arg_bytes = inputs[step]
        arg = arg_bytes.decode('utf-8')
        result_bytes = outputs[step]
        result = result_bytes.decode('utf-8')
        print("{}(*{}) -> {}".format(name, arg, result))


class Cache:
    """
    Redis Cache
    """
    def __init__(self):
        """Initialize an instance"""
        self._redis = redis.Redis()
        # Delete everything stored in this database
        self._redis.flushdb()

    @call_history
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
