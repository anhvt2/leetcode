class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pointer = 0
        for num in nums:
            if num != 0:
                nums[pointer] = num
                pointer += 1
        for i in range(pointer, len(nums)):
            nums[i] = 0
