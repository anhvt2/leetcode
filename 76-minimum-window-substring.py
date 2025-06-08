
from typing import List, Optional
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        t_count = Counter(t)
        window_count = Counter()
        l, r = 0, 0
        min_len = float('inf')
        min_window = ""
        
        while r < len(s):
            window_count[s[r]] += 1
            r += 1
            
            while all(window_count[char] >= t_count[char] for char in t_count):
                if r - l < min_len:
                    min_len = r - l
                    min_window = s[l:r]
                
                window_count[s[l]] -= 1
                l += 1
        
        return min_window

s = "ADOBECODEBANC"
t = "ABC"

