"""
LeetCode 2975: Maximum Square Area by Removing Fences From a Field

Problem:
Given a rectangular field (m-1) x (n-1) with corners at (1,1) and (m,n).
- Horizontal fences: from (hFences[i], 1) to (hFences[i], n)
- Vertical fences: from (1, vFences[i]) to (m, vFences[i])
- Field is surrounded by boundary fences that cannot be removed
- Find maximum area of a square field by removing some fences
- Return result modulo 10^9 + 7, or -1 if impossible

Key Insight:
To form a square, we need equal distances between horizontal and vertical fences.
1. Calculate all possible distances between pairs of horizontal fences (including boundaries)
2. Calculate all possible distances between pairs of vertical fences (including boundaries)
3. Find the maximum distance that exists in both sets
4. Return distance^2 mod (10^9 + 7)
"""

from typing import List, Set
from itertools import combinations

class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        MOD = 10**9 + 7
        
        def get_all_distances(fences: List[int], boundary: int) -> Set[int]:
            """
            Calculate all possible distances between fence pairs.
            Include boundary fences at positions 1 and boundary.
            """
            # Add boundary fences
            fences_with_boundaries = fences + [1, boundary]
            fences_with_boundaries.sort()
            
            # Calculate all pairwise distances
            distances = set()
            for i in range(len(fences_with_boundaries)):
                for j in range(i + 1, len(fences_with_boundaries)):
                    distance = fences_with_boundaries[j] - fences_with_boundaries[i]
                    distances.add(distance)
            
            return distances
        
        # Get all possible horizontal distances (side lengths)
        h_distances = get_all_distances(hFences, m)
        
        # Get all possible vertical distances (side lengths)
        v_distances = get_all_distances(vFences, n)
        
        # Find common distances (valid square side lengths)
        common_distances = h_distances & v_distances
        
        # Return maximum square area
        if not common_distances:
            return -1
        
        max_side = max(common_distances)
        return (max_side * max_side) % MOD