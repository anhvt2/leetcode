# Treat nums as a linked list, where:
# Each nums[i] is a pointer to the next index. Since there's a duplicate, there's a cycle.
# Use Floyd’s algorithm to detect the cycle start, which is the duplicate number.

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Phase 1: Detect intersection point
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Phase 2: Find entrance to the cycle (duplicate)
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow # or fast
