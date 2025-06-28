class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        # Step 1: Find the first decreasing element from the end
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        # Step 2: If there is a decreasing element, find the element to swap with
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            
            # Step 3: Swap the elements
            nums[i], nums[j] = nums[j], nums[i]
        
        # Step 4: Reverse the sublist after the index i
        nums[i + 1:] = reversed(nums[i + 1:])
