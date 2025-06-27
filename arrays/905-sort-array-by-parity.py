from collections import deque
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        queue = deque()
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                queue.append(nums[i])
            else:
                queue.appendleft(nums[i])
        return list(queue)
