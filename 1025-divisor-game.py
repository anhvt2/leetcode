class Solution:
    def divisorGame(self, n: int) -> bool:
        # Alice wins IFF n is even
        # if n = 1: no legal move, Alice loses
        # if n = 2: Alice picks x = 1, then Bob loses
        # if n = 2k: Alice picks x = 1, 
        #               then 2k-1 is odd, 
        #               then any x Bob picks is odd, 
        #               then 2k-1-x is even
        #               then Alice picks 1 again, and Bob always has an odd
        return True if n % 2 == 0 else False
