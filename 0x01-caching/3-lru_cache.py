#!/usr/bin/python3
"""BaseCaching module
"""

from base_caching import BaseCaching

class LRUCache(Basecaching):
    def __init__(self):
        """
        init
        """
        super().__init__()
        self.usage_count() = {}
    
    def put(self, key, item):
        """
        docs
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if key not in self.cache_data:
                least_used = min(self.usage_count, key=self.usage_count.get)
                del self.cache_data[least_used]
                del self.usage_count[least_used]
                print(f"DISCARD: {least_used}")
            
        self.cache_data[key] = item
        self.usage_count[key] = self.usage_count.get(key, 0) + 1
    
    def get(self, key):
        """
        docs
        """
        if key is None or key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]

