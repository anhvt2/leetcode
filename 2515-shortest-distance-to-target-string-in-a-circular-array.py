class Solution:
    def closestTarget(self, words, target, startIndex):
        """
        Key idea:
        - Circular array → distance between i and startIndex is:
              min(|i - startIndex|, n - |i - startIndex|)
        - Just check all positions where words[i] == target.

        This avoids the "i ± n" trick and is much cleaner.
        """

        n = len(words)
        ans = float('inf')

        for i, w in enumerate(words):
            if w == target:
                d = abs(i - startIndex)
                # take shorter direction around the circle
                ans = min(ans, min(d, n - d))

        return -1 if ans == float('inf') else ans