class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        """
        Greedy Approach: O(n) time, O(1) space
        
        Key Insight:
        - Start with target[0] operations (we need at least this many)
        - For each subsequent element, if it's higher than previous,
          we need (target[i] - target[i-1]) additional operations
        - If it's lower or equal, we can "reuse" previous operations
        
        Think of it as building blocks from left to right:
        [3, 1, 1, 2]
         ███
         ███     █
         ███ █ █ █
        
        We need 3 ops to build first column, then existing operations
        already cover the 1s, then we need 1 more operation for the last 2.
        """
        operations = 0
        prev = 0
        
        for num in target:
            operations += max(0, num - prev)
            prev = num
        
        return operations
