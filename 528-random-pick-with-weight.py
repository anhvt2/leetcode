import bisect
import random

class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sums = []
        total = 0
        for weight in w:
            total += weight
            self.prefix_sums.append(total)
        self.total = total

    def pickIndex(self) -> int:
        target = random.randint(1, self.total)
        return bisect.bisect_left(self.prefix_sums, target)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
