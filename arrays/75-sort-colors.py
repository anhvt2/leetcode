class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # return nums.sort()
        low, i, high = 0, 0, len(nums) - 1
        # [0, ..., low-1]: all 0
        # [low, ..., i-1]: all 1
        # [i, ..., high]: unknown
        # [high+1, ..., end]: all 2
        while i <= high:
            if nums[i] == 0:
                nums[i], nums[low] = nums[low], nums[i]
                low += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[high] = nums[high], nums[i]
                high -= 1
            elif nums[i] == 1:
                i += 1
