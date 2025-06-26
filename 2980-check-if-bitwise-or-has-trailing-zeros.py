class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        # Count how many even numbers there are in the list
        even_count = sum(1 for num in nums if num % 2 == 0)
        
        # If there are at least two even numbers, the OR will have a trailing zero
        return even_count >= 2
