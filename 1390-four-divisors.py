class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        """
        Algorithm:
        ----------
        For each number x in nums:
        - Enumerate divisors up to sqrt(x)
        - Collect divisors in pairs (d, x//d)
        - If the total number of distinct divisors is exactly 4,
          add their sum to the answer.

        Optimization:
        - Stop early if more than 4 divisors are found.

        Complexity:
        - Time: O(n * sqrt(max(nums)))
        - Space: O(1) extra
        """
        import math

        ans = 0

        for x in nums:
            divs = set()
            for d in range(1, int(math.sqrt(x)) + 1):
                if x % d == 0:
                    divs.add(d)
                    divs.add(x // d)
                    if len(divs) > 4:
                        break

            if len(divs) == 4:
                ans += sum(divs)

        return ans
