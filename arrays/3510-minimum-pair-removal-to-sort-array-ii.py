from typing import List
import heapq

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        # Doubly linked list via indices
        left = [-1] * n
        right = [-1] * n
        for i in range(n):
            left[i] = i - 1
            right[i] = i + 1 if i + 1 < n else -1

        removed = [False] * n

        # Count monotonicity violations
        violations = 0
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                violations += 1

        # Min-heap of (sum, index)
        heap = []
        for i in range(n - 1):
            heapq.heappush(heap, (nums[i] + nums[i + 1], i))

        ops = 0

        while violations > 0:
            pair_sum, i = heapq.heappop(heap)
            j = right[i]

            # Hard validity checks
            if (
                j == -1 or
                removed[i] or removed[j] or
                nums[i] + nums[j] != pair_sum
            ):
                continue

            li = left[i]
            rj = right[j]

            # Remove old violations
            if li != -1 and nums[li] > nums[i]:
                violations -= 1
            if nums[i] > nums[j]:
                violations -= 1
            if rj != -1 and nums[j] > nums[rj]:
                violations -= 1

            # Merge
            nums[i] += nums[j]
            removed[j] = True
            right[i] = rj
            if rj != -1:
                left[rj] = i

            # Add new violations
            if li != -1 and nums[li] > nums[i]:
                violations += 1
            if rj != -1 and nums[i] > nums[rj]:
                violations += 1

            # Push updated adjacent pairs
            if li != -1:
                heapq.heappush(heap, (nums[li] + nums[i], li))
            if rj != -1:
                heapq.heappush(heap, (nums[i] + nums[rj], i))

            ops += 1

        return ops
