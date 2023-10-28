#!/usr/bin/env python3
"""
Module that defines a class for interacting with Redis.
"""
import uuid
import redis
import functools
from typing import Callable


def count_calls(method: Callable) -> Callable:
    """
    Decorator that counts the number of times a method is called.

    Args:
        method (Callable): The method to be decorated.

    Returns:
        Callable: The decorated method.
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__  # Using the qualified name of the method as the key
        self._redis.incr(key)  # Increment the count for the key in Redis
        return method(self, *args, **kwargs)  # Call the original method and return its result

    return wrapper


class Cache:
    """
    Cache class for storing data in Redis.

    Attributes:
        _redis (redis.Redis): An instance of the Redis client.
    """

    def __init__(self):
        """
        Initializes the Cache object.
        Creates an instance of the Redis client and flushes the Redis database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: str) -> str:
        """
        Stores the input data in Redis with a randomly generated key.

        Args:
            data (str): The data to be stored in Redis.

        Returns:
            str: The randomly generated key used to store the data in Redis.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
