class MyHashMap:

    def __init__(self):
        # Use a dictionary to store key-value pairs
        self.hash_map = {}

    def put(self, key: int, value: int) -> None:
        # Insert key-value pair into the dictionary
        self.hash_map[key] = value

    def get(self, key: int) -> int:
        # Return the value if the key exists, otherwise return -1
        return self.hash_map.get(key, -1)

    def remove(self, key: int) -> None:
        # Remove the key from the dictionary if it exists
        if key in self.hash_map:
            del self.hash_map[key]
