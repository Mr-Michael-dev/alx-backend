#!/usr/bin/python3
"""
class LFUCache that inherits from BaseCaching and is a caching system
"""
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    This class implements put and get methods that
    adds or retrieves data from self.cache_data in the BaseCache
    using the LFU policy
    """

    def __init__(self):
        """
        instantiation method
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        assign to the dictionary self.cache_data the item value for the key
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                # Update existing key, move to end
                del self.cache_data[key]
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Remove the first inserted key
                MR_key= next(reversed(self.cache_data))
                print(f"DISCARD: {MR_key}")
                del self.cache_data[MR_key]
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)

    def get(self, key):
        """
        return the value in self.cache_data linked to key

        Arguments:
        key: key to the cached data
        """

        if key is not None and key in self.cache_data.keys():
            self.cache_data.move_to_end(key, last=False)
            return self.cache_data[key]
        return None
