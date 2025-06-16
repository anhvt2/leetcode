
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prod = 1
        zero_idxs = []
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_idxs.append(i)
            else:
                prod *= nums[i] # product of non-zero elements

        # if there are at least two zeros then all are zeros
        if len(zero_idxs) > 1:
            return [0] * n

        # real algo
        elif len(zero_idxs) == 1:
            answer = []
            for i in range(n):
                if nums[i] != 0:
                    answer.append(0)
                else: # nums[i] != 0
                    answer.append(prod)
                    
        else: # len(zeros_idxs) == 0 
            answer = []
            for i in range(n):
                answer.append(prod // nums[i])

        return answer

