"""
LeetCode 2528: Maximize the Minimum Powered City
Fixed and Fully Annotated Solution
"""

from typing import List
from itertools import accumulate


class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        """
        🛠️ Solution Strategy
        1. Binary Search on Minimum Power
            - Define search space: from min possible power to theoretical max
            - Find the highest minimum power achievable with k additional stations
        2. Greedy Check Function
            - For each candidate minimum power, verify if achievable with ≤ k stations
            - Use difference array + sliding window to track power coverage
            - Place new stations greedily at rightmost positions for max future coverage
        
        Time: O(n * log(maxPower))
        Space: O(n)
        """
        n = len(stations)
        
        # Step 1: Build difference array to calculate initial power distribution
        # df[i] represents the change in power count at position i
        df = [0] * (n + 5)  # Extra space to avoid index out of bounds
        
        for i, station_count in enumerate(stations):
            # Each station at position i covers [i-r, i+r]
            # Add station_count at the left boundary of coverage
            left_boundary = max(0, i - r)
            df[left_boundary] += station_count
            
            # Subtract at right boundary + 1 (difference array technique)
            right_boundary = min(n - 1, i + r)
            df[right_boundary + 1] -= station_count
        
        # Step 2: Set up binary search bounds
        # lo: minimum possible power (the weakest city currently)
        # hi: theoretical maximum (large enough to cover all cases)
        lo = min(accumulate(df[:n]))  # Current minimum power across all cities
        hi = 2 * 10 ** 10             # Upper bound (sum of all + k would work too)
        
        def check(target_min_power: int) -> bool:
            """
            Check if we can achieve target_min_power as minimum using ≤ k stations.
            
            Strategy: Scan left to right, whenever a city falls below target,
            add stations at the rightmost position that can still cover this city.
            This greedy placement maximizes coverage for future cities.
            
            Args:
                target_min_power: The minimum power we're trying to achieve
                
            Returns:
                True if achievable with ≤ k stations, False otherwise
            """
            # Create a copy of difference array for this attempt
            diff = df[:]
            
            current_power = 0  # Running sum of power at current position
            stations_used = 0  # Count of additional stations placed
            
            for i in range(n):
                # Update current power using difference array
                current_power += diff[i]
                
                # If current city is below target, we need to add stations
                if current_power < target_min_power:
                    deficit = target_min_power - current_power
                    stations_used += deficit
                    
                    # Early termination: exceeded our budget
                    if stations_used > k:
                        return False
                    
                    # Place stations at rightmost position that can cover city i
                    # This position is min(n-1, i + r)
                    # But these stations also have their own range, so they affect
                    # cities up to position: min(n-1, i + r) + r = min(n-1, i + 2r)
                    placement_pos = min(n - 1, i + r)
                    coverage_end = min(n - 1, placement_pos + r)
                    
                    # Update difference array: stations stop affecting after coverage_end
                    diff[coverage_end + 1] -= deficit
                    
                    # Immediately apply the boost to current_power
                    current_power = target_min_power
            
            return True
        
        # Step 3: Binary search to find maximum achievable minimum power
        while lo < hi:
            # Calculate mid with ceiling division to avoid infinite loop
            mid = (lo + hi + 1) >> 1  # Equivalent to (lo + hi + 1) // 2
            
            if check(mid):
                # Can achieve mid, try higher
                lo = mid
            else:
                # Cannot achieve mid, try lower
                hi = mid - 1
        
        return lo
