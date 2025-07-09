class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        cost_even = 0
        cost_odd = 0
        for i in range(len(position)):
            if position[i] % 2 == 1:
                cost_odd += 1
            else:
                cost_even += 1
        return min(cost_even, cost_odd)
