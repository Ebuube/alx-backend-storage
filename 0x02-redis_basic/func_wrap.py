#!/usr/bin/env python3
"""Learn how to wrap a function"""
from functools import wraps


def list_params(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        print("Calling decorated function")
        print("Args")
        for arg in args:
            print(arg)
        if kwargs:
            print("Kwargs\n{}".format(**kwargs))
        print("Decorated funtion done")
        return f(*args, **kwargs)

    return wrapper


@list_params
def sum(a, b):
    print("{} + {} = {}".format(a, b, a + b))


sum(5, 9)


@list_params
def diff(a, b):
    print("{} - {} = {}".format(a, b, a - b))

diff(12, 3)
