class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        """
        Key idea:
        - We want two houses with different colors.
        - Max distance means we should always compare:
            1) first element vs farthest possible
            2) last element vs farthest possible

        Because optimal pair always involves an endpoint.
        """

        n = len(colors)

        # if endpoints differ, that's the maximum possible
        if colors[0] != colors[-1]:
            return n - 1

        # otherwise, try shrinking from both sides
        # find farthest index differing from first color
        left = 0
        while colors[left] == colors[0]:
            left += 1

        right = n - 1
        while colors[right] == colors[-1]:
            right -= 1

        return max(n - 1 - left, right)