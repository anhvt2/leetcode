class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        arr = nums[:]
        operations = 0
        
        # Check if array is non-decreasing
        def is_sorted(a):
            return all(x <= y for x, y in pairwise(a))
        
        # Keep merging until sorted
        while not is_sorted(arr):
            # Find the leftmost pair with minimum sum
            min_sum = float('inf')
            min_index = 0
            
            for i in range(len(arr) - 1):
                pair_sum = arr[i] + arr[i + 1]
                if pair_sum < min_sum:
                    min_sum = pair_sum
                    min_index = i
            
            # Merge the pair: replace arr[min_index] with sum, remove arr[min_index+1]
            arr[min_index] = min_sum
            arr.pop(min_index + 1)
            operations += 1
        
        return operations