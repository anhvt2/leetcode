from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        child = 0
        cookie = 0
        
        while child < len(g) and cookie < len(s):
            if s[cookie] >= g[child]:
                # Cookie satisfies the current child
                child += 1
            # Whether or not the cookie was used, move to next cookie
            cookie += 1
        
        return child  # Number of happy children
