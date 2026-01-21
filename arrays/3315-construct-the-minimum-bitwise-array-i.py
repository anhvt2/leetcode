from typing import List
class Solution:
    def minBitwiseArray(self, nums: list[int]) -> list[int]:
        ans = []
        
        for num in nums:
            # Find minimum x such that x OR (x + 1) == num
            
            min_x = -1
            
            # Try turning off each 1 bit in num
            for bit in range(32):
                if num & (1 << bit):  # If this bit is 1 in num
                    # Try x = num with this bit turned off
                    x = num ^ (1 << bit)
                    
                    # Check if x OR (x + 1) == num
                    if (x | (x + 1)) == num:
                        if min_x == -1 or x < min_x:
                            min_x = x
            
            ans.append(min_x)
        
        return ans