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
