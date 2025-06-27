class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        output = []
        set_nums = set(nums)
        for i in range(1, len(nums)+1):
            if i not in set_nums:
                output.append(i)
            
        return output
