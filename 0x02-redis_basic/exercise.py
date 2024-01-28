#!/usr/bin/env python3

""" Writing strings to Redis """

import redis
from uuid import uuid4
from functools import wraps


def count_calls(method: callable) -> callable:
    """count how many times methods"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """wrapper function"""
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: callable) -> callable:
    """ "call history"""

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """wrapper function"""
        self._redis.rpush("{}:inputs".format(method.__qualname__), str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush("{}:outputs".format(method.__qualname__), result)
        return result

    return wrapper


class Cache:
    """Cache class"""

    def __init__(self) -> None:
        """Constructor method"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: any) -> str:
        """Method that store data in redis"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: callable = None) -> any:
        """Method that get data from redis"""
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """Method that get data from redis"""
        data = self._redis.get(key)
        return data.decode("utf-8")

    def get_int(self, key: str) -> int:
        """Method that get data from redis"""
        data = self._redis.get(key)
        return int(data)
