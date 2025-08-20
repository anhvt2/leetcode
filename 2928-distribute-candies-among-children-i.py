class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        result = 0
        for i in range(0, limit + 1):           
            for j in range(0, limit + 1):
                k = n - i - j  # Calculate k directly
                if 0 <= k <= limit:  # Check if k is valid
                    result += 1
        return result
