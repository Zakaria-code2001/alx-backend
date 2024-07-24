#!/usr/bin/python3
"""BaseCaching module"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRU (Least Recently Used) caching system"""

    def __init__(self):
        """Initialize LRUCache"""
        super().__init__()
        self.usage_count = {}

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
                least_used = min(self.usage_count, key=self.usage_count.get)
                del self.cache_data[least_used]
                del self.usage_count[least_used]
                print(f"DISCARD: {least_used}")

        self.cache_data[key] = item
        self.usage_count[key] = self.usage_count.get(key, 0) + 1

    def get(self, key):
        """
        Retrieve an item from the cache
        
        Args:
            key: The key of the item to retrieve

        Returns:
            The cached item if it exists, None otherwise
        """
        if key is None or key not in self.cache_data:
            return None

        self.usage_count[key] += 1
        return self.cache_data[key]