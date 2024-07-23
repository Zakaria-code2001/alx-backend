#!/usr/bin/python3
""" BaseCaching module
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    def __init__(self):
        super().__init__(self.cache_data)
    
    def put(self, key, item):
        if key == None and item == None:
            pass
        else:
            self.cache_data[key] = item
    
    def get(self, key):
        if key not in self.cache_data or key == None:
            return None
        else:
            return self.cache_data[key]