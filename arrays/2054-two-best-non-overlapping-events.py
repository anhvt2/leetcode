from typing import List
import bisect

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        """
        Algorithm:
        ----------
        1. Sort events by start time.
        2. Build a suffix array where suffixMax[i] is the maximum event value
           from index i onward.
        3. For each event:
           - Use binary search to find the first event that starts after
             the current event ends.
           - Combine their values.
        4. Track the maximum result.

        Time Complexity: O(n log n)
        Space Complexity: O(n)
        """

        # Sort events by start time
        events.sort(key=lambda x: x[0])

        n = len(events)
        starts = [e[0] for e in events]

        # suffixMax[i] = max value among events[i:]
        suffixMax = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffixMax[i] = max(suffixMax[i + 1], events[i][2])

        ans = 0

        for i in range(n):
            start, end, value = events[i]

            # Find the first event with start > end
            j = bisect.bisect_right(starts, end)

            # Combine values
            ans = max(ans, value + suffixMax[j])

        return ans
