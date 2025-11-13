from collections import Counter

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        
        def sum_top_x(arr, x):
            count_dict = collections.Counter(arr)
            count_sorted = sorted(count_dict.items(), key = lambda item: (-item[1], -item[0]))
            if len(count_sorted) <= x:
                return sum([i[0]*i[1] for i in count_sorted])
            else:
                return sum([i[0]*i[1] for i in count_sorted[:x]])
        
        res = []
        n = len(nums)
        for i in range(n-k+1):
            res.append(sum_top_x(nums[i:i+k], x))
        
        return res
