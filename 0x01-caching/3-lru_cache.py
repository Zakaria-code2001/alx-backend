#!/usr/bin/python3
"""BaseCaching module"""

from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """LRU (Least Recently Used) caching system"""

    def __init__(self):
        """Initialize LRUCache"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Add an item to the cache
        
        Args:
            key: The key to store the item under
            item: The item to store in the cache
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            if key not in self.cache_data:
                lru_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", lru_key)
                

        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=False)

    def get(self, key):
        """
        Retrieve an item from the cache
        
        Args:
            key: The key of the item to retrieve

        Returns:
            The cached item if it exists, None otherwise
        """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
