class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # https://www.geeksforgeeks.org/python/python-program-for-largest-sum-contiguous-subarray/
        max_so_far = float('-inf')
        max_ending_here = 0
         
        for i in range(0, len(nums)):
            max_ending_here = max_ending_here + nums[i]
            if (max_so_far < max_ending_here):
                max_so_far = max_ending_here
            if max_ending_here < 0:
                max_ending_here = 0   
        return max_so_far

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane algorithm: https://en.wikipedia.org/wiki/Maximum_subarray_problem
        best_sum = -float('inf')  # Initialize to a very small number
        current_sum = 0
        for x in nums:
            # Update the current_sum to be the maximum of the current element alone or adding it to the current_sum
            current_sum = max(x, current_sum + x)
            # # Update the best_sum to store the maximum value encountered so far
            best_sum = max(best_sum, current_sum)
        
        # Return the best_sum after the loop has finished processing all elements
        return best_sum
