#!/usr/bin/python3
""" BaseCaching module
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    class BasicCache that
    inherits from BaseCaching
    and is a caching system
    """

    def put(self, key, item):
        """
        put item
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        get item
        """
        if key is None:
            return None
        return self.cache_data[key]
