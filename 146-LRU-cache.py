from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            # Move to end to mark as recently used
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Remove it first to update order
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            # Pop the least recently used item (first one)
            self.cache.popitem(last=False)


# Your LRUCache object will be instantiated and called as such:
capacity = ["LRUCache","put","put","get","put","get","put","get","get","get"]

obj = LRUCache(capacity)
param_1 = obj.get(key)
obj.put(key,value)


