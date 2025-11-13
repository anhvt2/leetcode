from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        """
        Optimized O(n) solution using stack-based approach.
        
        Key insight: Track the number of distinct values we need to "peel off"
        as we traverse the array. Each increase in values requires additional operations.
        """
        n = len(nums)
        if n == 0:
            return 0
        
        operations = 0
        stack = []
        
        for num in nums:
            # Remove all values from stack that are greater than current
            # (we've finished processing those ranges)
            while stack and stack[-1] > num:
                stack.pop()
            
            # If current num is 0 or already in stack, skip
            if num == 0 or (stack and stack[-1] == num):
                continue
            
            # New value encountered - need one more operation
            stack.append(num)
            operations += 1
        
        return operations
