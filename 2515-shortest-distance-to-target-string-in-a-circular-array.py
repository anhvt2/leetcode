class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        ds = []
        n = len(words)
        for i, word in enumerate(words):
            if word == target:
                ds.append(abs(i - startIndex))
                ds.append(abs(i - n - startIndex))
                ds.append(abs(i + n - startIndex))
        if not ds:
            return -1
        
        min_d = float('inf')
        for d in ds:
            if d < min_d:
                min_d = d
        return min_d