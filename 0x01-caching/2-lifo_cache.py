#!/usr/bin/python3
"""
class LIFOCache that inherits from BaseCaching and is a caching system
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    This class implements put and get methods that
    adds or retrieves data from self.cache_data in the BaseCache
    using the LIFO policy
    """

    def __init__(self):
        """
        instantiation method
        """
        super().__init__()

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
                oldest_key, oldest_item = self.cache_data.popitem()
                print(f"DISCARD: {oldest_key}")
            self.cache_data[key] = item

    def get(self, key):
        """
        return the value in self.cache_data linked to key

        Arguments:
        key: key to the cached data
        """

        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
