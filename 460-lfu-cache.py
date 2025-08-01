from collections import defaultdict, OrderedDict

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_val_freq = {}  # key -> (val, freq)
        self.freq_to_keys = defaultdict(OrderedDict)  # freq -> {key: None}
        self.min_freq = 0

    def get(self, key: int) -> int:
        if key not in self.key_to_val_freq:
            return -1

        val, freq = self.key_to_val_freq[key]

        # Remove key from current freq list
        del self.freq_to_keys[freq][key]

        # If that was the last key with min_freq, update min_freq
        if not self.freq_to_keys[freq]:
            if self.min_freq == freq:
                self.min_freq += 1
            del self.freq_to_keys[freq]

        # Increase frequency
        self.freq_to_keys[freq + 1][key] = None
        self.key_to_val_freq[key] = (val, freq + 1)

        return val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        # If key exists, update its value and call get() to update freq
        if key in self.key_to_val_freq:
            self.key_to_val_freq[key] = (value, self.key_to_val_freq[key][1])  # update value
            self.get(key)  # also increases frequency
            return

        # Evict if at capacity
        if len(self.key_to_val_freq) >= self.capacity:
            # Remove the LRU key in min_freq
            evict_key, _ = self.freq_to_keys[self.min_freq].popitem(last=False)
            del self.key_to_val_freq[evict_key]

        # Insert new key
        self.freq_to_keys[1][key] = None
        self.key_to_val_freq[key] = (value, 1)
        self.min_freq = 1  # reset min_freq for new key
