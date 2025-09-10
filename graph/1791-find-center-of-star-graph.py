class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        seen = set()
        for u, v in edges:
            if u not in seen:
                seen.add(u)
            else:
                return u
            if v not in seen:
                seen.add(v)
            else:
                return v