class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        
        # Try all possible subarrays
        for i in range(n):
            seen_even = set()
            seen_odd = set()
            
            for j in range(i, n):
                # Add current element to the subarray
                if nums[j] % 2 == 0:
                    seen_even.add(nums[j])
                else:
                    seen_odd.add(nums[j])
                
                # Check if balanced
                if len(seen_even) == len(seen_odd):
                    ans = max(ans, j - i + 1)
        
        return ans