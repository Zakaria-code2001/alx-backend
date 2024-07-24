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

    class BasicCache(BaseCaching):
    '''A class `BasicCache` that inherits from `BaseCaching`
       and is a caching system
    '''

    def put(self, key, item):
        """
        put
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        get
        """

        return self.cache_data.get(key, None)
