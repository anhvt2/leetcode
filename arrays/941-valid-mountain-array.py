class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        
        # A mountain array needs at least 3 elements
        if n < 3:
            return False
        
        # Find the peak: It must not be the first or last element
        i = 0
        while i + 1 < n and arr[i] < arr[i + 1]:
            i += 1
        
        # The peak must not be the first or last element
        if i == 0 or i == n - 1:
            return False
        
        # Check the decreasing part of the array
        while i + 1 < n and arr[i] > arr[i + 1]:
            i += 1
        
        # If we have gone through the entire array, it's a valid mountain array
        return i == n - 1

# class Solution:
#     def validMountainArray(self, arr: List[int]) -> bool:
#         if len(arr) < 3:
#             return False
#         elif len(arr) == 3:
#             return True if arr[1] > arr[0] and arr[2] < arr[1] else False
#         else:
#             count = 0 # number of changes
#             # when count = 0: monotonic increasing
#             # when count = 1: monotonic decreasing
#             for i in range(1, len(arr)-1):
#                 if arr[i-1] < arr[i] and arr[i] > arr[i+1] and count == 0:
#                     count = 1
#                 if arr[i] > arr[i+1] and count == 0:
#                     return False
#                 if arr[i] < arr[i+1] and count == 1:
#                     return False
#             return True if count == 1 else False