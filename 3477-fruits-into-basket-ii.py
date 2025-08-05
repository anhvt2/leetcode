class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n, m = len(fruits), len(baskets)
        used = [False] * m
        unplaced = 0

        # Try to place fruit i in basket j
        for fruit in fruits:
            placed = False
            for j in range(m):
                if not used[j] and baskets[j] >= fruit:
                    used[j] = True
                    placed = True
                    break
            if not placed:
                unplaced += 1
        return unplaced
