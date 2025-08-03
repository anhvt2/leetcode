from collections import defaultdict
import bisect

class TimeMap:
    def __init__(self):
        # key -> {'timestamps': [...], 'values': [...]}
        self.store = defaultdict(lambda: {'timestamps': [], 'values': []})

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key]['timestamps'].append(timestamp)
        self.store[key]['values'].append(value)

    def get(self, key: str, timestamp: int) -> str:
        data = self.store[key]
        timestamps = data['timestamps']
        values = data['values']

        # Find the rightmost timestamp <= given timestamp
        idx = bisect.bisect_right(timestamps, timestamp)
        if idx == 0:
            return ""
        return values[idx - 1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)