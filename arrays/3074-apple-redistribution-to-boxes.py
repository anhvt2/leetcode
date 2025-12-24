from typing import List

class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        """
        Algorithm:
        ----------
        1. Compute the total number of apples.
        2. Sort box capacities in descending order.
        3. Greedily select the largest boxes until total capacity
           covers all apples.
        4. Return the number of boxes used.

        Time Complexity: O(m log m)
        Space Complexity: O(1)
        """

        total_apples = sum(apple)

        # Sort capacities from largest to smallest
        capacity.sort(reverse=True)

        current_capacity = 0
        boxes_used = 0

        for cap in capacity:
            current_capacity += cap
            boxes_used += 1
            if current_capacity >= total_apples:
                return boxes_used

        # Problem guarantees enough capacity exists
        return boxes_used
