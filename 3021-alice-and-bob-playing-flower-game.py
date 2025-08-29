class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        # (x, y) is valid if one is odd and another one is even
        # x \in [1,n], y \in [1,m]
        # Count odds and evens for two lanes

        def countOddEven(z): # count odds and evens between [1,z]
            if z % 2 == 1:
                odds = (z - 1) // 2 + 1
                evens = odds - 1 #  (z - 3) // 2 + 1
            else: # z % 2 == 0
                odds = (z - 2) // 2 + 1
                evens = odds # (z - 2) // 2 + 1
            return odds, evens
        
        odd_n, even_n = countOddEven(n)
        odd_m, even_m = countOddEven(m)
        return odd_n * even_m + even_n * odd_m
        