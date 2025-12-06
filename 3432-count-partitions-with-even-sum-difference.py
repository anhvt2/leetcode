from typing import List

class Solution:
	def countPartitions(self, nums: List[int]) -> int:
		"""
		Return the number of split indices i (0 <= i < n-1) where
		difference between left and right sums is even.
		"""
		n = len(nums)
		if n < 2:
			return 0 # no valid split when array length < 2

		total = sum(nums)
		
		# If total is even, every split index 0..n-2 yields an even difference.
		return (n - 1) if (total % 2 == 0) else 0