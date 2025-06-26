class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        kidx = []
        i = 0
        j = 0
        while i < len(nums):
            i_next = i + 1
            if nums[i] == key:
                i_next = i + k + 1
                j = max(j, i - k)
                while j < min(i + k + 1, len(nums)):
                    if nums[j] == key:
                        i_next = j
                    kidx.append(j)
                    j += 1
            i = i_next
        return kidx


# class Solution:
#     def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
#         result = set()
        
#         # Find all indices where nums[j] == key
#         key_indices = [i for i, num in enumerate(nums) if num == key]
        
#         # For each index of the 'key', add indices within distance 'k' to result
#         for j in key_indices:
#             for i in range(max(0, j - k), min(len(nums), j + k + 1)):
#                 result.add(i)
        
#         # Convert set to list and return sorted (optional, if you need sorted output)
#         return sorted(result)
