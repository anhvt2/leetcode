from collections import defaultdict
class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        value_map = defaultdict(list)
        for xi, yi in zip(x, y):
            value_map[xi].append(yi)

        sorted_y_values = []
        for values in value_map.values():
            values.sort(reverse=True)
            sorted_y_values.append(values[0])
        
        if len(sorted_y_values) < 3:
            return -1
        
        sorted_y_values.sort(reverse=True)
        return sum(sorted_y_values[:3])
