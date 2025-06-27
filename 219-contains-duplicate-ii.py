class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}
        for i in range(len(nums)):
            if nums[i] in seen and i - seen[nums[i]] <= k:
                return True
            seen[nums[i]] = i
        return False

# class Solution:
#     def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
#         # Set to store unique elements in the sliding window
#         seen = set()
        
#         for i in range(len(nums)):
#             # If the number is already in the set, return True
#             if nums[i] in seen:
#                 return True
#             # Add the current number to the set
#             seen.add(nums[i])
            
#             # If the size of the set exceeds k, remove the element that is out of range
#             if len(seen) > k:
#                 seen.remove(nums[i - k])
        
#         # No duplicates found within range k
#         return False


# from collections import deque
# class Solution:
#     def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
#         seen = deque()
#         if k == 0:
#             return False
#         for i in range(len(nums)):
#             if nums[i] in seen:
#                 return True
#             if len(seen) < k:
#                 seen.append(nums[i])
#             else:
#                 seen.popleft()
#                 seen.append(nums[i])
#         return False
#         