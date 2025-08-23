class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        # A special string can be uniquely split into primitive blocks where the running balance #1 - #0 returns to 0.
        # For each primitive block "1 ... 0", recursively maximize the inside, then sort all resulting
        # blocks in descending lexicographic order and join them. That yields the global maximum.
        parts = []
        bal = 0
        start = 0
        # Split into primitive special substrings
        for i, ch in enumerate(s):
            bal += 1 if ch == '1' else -1
            if bal == 0:
                # s[start:i+1] looks like "1 <inner> 0"
                inner = s[start+1:i]
                parts.append('1' + self.makeLargestSpecial(inner)  + '0')
                start = i + 1
        
        # Greedily take the largest arrangement
        parts.sort(reverse=True)
        return ''.join(parts)