from typing import List

class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        # Build 1-indexed sets of languages per user
        m = len(languages)
        knows = [set()] * (m + 1)
        for i, langs in enumerate(languages, start=1):
            knows[i] = set(langs)

        # Step 1: find friendships that can't currently communicate
        broken = []
        for u, v in friendships:
            if knows[u].isdisjoint(knows[v]):
                broken.append((u, v))

        if not broken:
            return 0

        # Step 2: candidate users who are involved in broken friendships
        candidates = set()
        for u, v in broken:
            candidates.add(u)
            candidates.add(v)

        # Step 3: try teaching each language; count who in candidates lacks it
        ans = float('inf')
        for lang in range(1, n + 1):
            need = 0
            for user in candidates:
                if lang not in knows[user]:
                    need += 1
            ans = min(ans, need)

        return ans
