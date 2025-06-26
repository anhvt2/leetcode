class MyHashSet:

    def __init__(self):
        # Initialize an empty set to simulate the HashSet
        self.hash_set = set()

    def add(self, key: int) -> None:
        # Add the key to the set
        self.hash_set.add(key)

    def remove(self, key: int) -> None:
        # Remove the key from the set if it exists
        self.hash_set.discard(key)  # discard doesn't raise an error if the key doesn't exist

    def contains(self, key: int) -> bool:
        # Check if the key is in the set
        return key in self.hash_set

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
