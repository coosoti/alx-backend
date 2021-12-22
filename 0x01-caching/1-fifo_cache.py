#!/usr/bin/env python3
"""
This module contains class FIFOCache that inherits from BaseCache and
 is a caching system
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO class inheriting from BaseCache class"""
    def __init__(self):
        """class constructor"""
        super().__init__()
        self.cache_data_list = []

    def put(self, key, item):
        """
        add item into a cache
        Args:
            key(str): key of the item to add
            item: item to add
        Returns: None
        """
        if key and item:
            self.cache_data[key] = item
            self.cache_data_list.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                self.cache_data.pop(self.cache_data_list[0])
                print("DISCORD: {}".format(self.cache_data_list.pop(0)))

    def get(self, key):
        """
        retrieve an item from cache
        Args:
            key(str): key of the item to add
        Returns: item if the key exists, None otherwise
        """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
