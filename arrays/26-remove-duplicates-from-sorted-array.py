class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0  # If the array is empty, return 0
        
        count = 1  # Start the count with 1 because the first element is always unique
        for pointer in range(1, len(nums)):
            if nums[pointer] != nums[pointer - 1]:  # Check if current element is different from the previous one
                nums[count] = nums[pointer]  # Place the new unique element at the correct position
                count += 1  # Increment the count of unique elements
        
        return count  # Return the number of unique elements

# nums = [1, 1, 2, 2, 3]
# nums = [1, 2, 3, 2, 3]
