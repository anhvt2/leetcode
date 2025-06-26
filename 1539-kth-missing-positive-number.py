class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing_count = 0  # Track the number of missing elements
        current = 1  # Start checking from 1
        i = 0  # Pointer for the array
        
        while missing_count < k:
            if i < len(arr) and arr[i] == current:
                # If the current number is in arr, move to the next number in arr
                i += 1
            else:
                # If the current number is not in arr, it's a missing number
                missing_count += 1
            
            if missing_count == k:
                return current
            
            current += 1  # Move to the next number
        
        return current  # This will return the kth missing number


# class Solution:
#     def findKthPositive(self, arr: List[int], k: int) -> int:
#         tmp = []
#         i = 1
#         while len(tmp) < k:
#             if i not in arr:
#                 tmp.append(i)
#             i += 1
#         return tmp[-1]