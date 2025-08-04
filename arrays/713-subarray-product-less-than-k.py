from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
    	"""
    	Time: O(n) each element enters and leaves window at most once
    	Space: O(1)
    	"""
    	# Edge case:
    	if k <= 1:
    		return 0

    	prod = 1
    	count = 0
    	left = 0

    	# Expand the right end of window
    	for right, val in enumerate(nums):
    		prod *= val

    		# Shrink from the left if prod is too large
    		while prod >= k:
    			prod //= nums[left]
    			left += 1

    		# All subarrays ending at `right` and starting from any between [left ... right] will have prod < k. There are (right - left + 1) of them
    		count += right - left + 1
    	return count
