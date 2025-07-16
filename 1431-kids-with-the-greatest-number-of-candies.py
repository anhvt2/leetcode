class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        current_max = float('-inf')
        for i in range(len(candies)):
            current_max = max(current_max, candies[i])

        res = []
        for i, kid in enumerate(candies):
            if kid + extraCandies >= current_max:
                res.append(True)
            else:
                res.append(False)

        return res