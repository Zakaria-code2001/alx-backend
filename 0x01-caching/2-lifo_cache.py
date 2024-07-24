#!/usr/bin/python3
"""BaseCaching module
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    lifo cache
    """
    def __init__(self):
        """
        init
        """
        super().__init__()

    def put(self, key, item):
        """
        put docs
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if key not in self.cache_data:
                discarded = list(self.cache_data.keys())[-1]
                del self.cache_data[discarded]
                print(f"DISCARD: {discarded}")

        self.cache_data[key] = item

    def get(self, key):
        """
        get docs
        """
        if key is None or key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]
