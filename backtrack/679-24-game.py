class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        EPS = 1e-6

        def can24(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24) < EPS

            # try all unorder pairs i < j
            n = len(nums)
            for i in range(n):
                for j in range(i+1, n):
                    a, b = nums[i], nums[j]

                    cand = set()
                    cand.add(a+b)
                    cand.add(a-b)
                    cand.add(b-a)
                    cand.add(a*b)
                    if abs(b) > EPS:
                        cand.add(a/b)
                    if abs(a) > EPS:
                        cand.add(b/a)

                    # build the next list and recurse
                    next_num_base = [nums[k] for k in range(n) if k != i and k != j]
                    for c in cand:
                        if can24(next_num_base + [c]):
                            return True
            return False
        
        return can24([float(x) for x in cards])