class Solution:
    def longestBalanced(self, s: str) -> int:
        # Handle case 1: Single distinct character
        # All occurrences of same char are automatically balanced
        def singleChar(s: str) -> int:
            res = 0
            i, n = 0, len(s)
            while i < n:
                j = i + 1
                # Extend while same character
                while j < n and s[j] == s[i]:
                    j += 1
                res = max(res, j - i)
                i = j
            return res

        # Handle case 2: Two distinct characters
        # Use difference tracking: treat one char as +1, other as -1
        # When difference returns to same value, counts are equal
        def twoChars(s: str, a: str, b: str) -> int:
            res = 0
            i, n = 0, len(s)
            while i < n:
                # Skip characters not in {a, b}
                while i < n and s[i] not in (a, b):
                    i += 1
                # pos[d] = first index where difference = d
                pos = {0: i - 1}
                d = 0  # Difference: count(a) - count(b)
                while i < n and s[i] in (a, b):
                    d += 1 if s[i] == a else -1
                    # If we've seen this difference before, substring is balanced
                    if d in pos:
                        res = max(res, i - pos[d])
                    else:
                        pos[d] = i
                    i += 1
            return res

        # Handle case 3: Three distinct characters
        # Track (a-b, b-c) as state key
        # Same state means relative differences unchanged → all equal
        def threeChars(s: str) -> int:
            # pos[(diff_ab, diff_bc)] = first index with this state
            pos = {(0, 0): -1}
            cnt = Counter()
            res = 0
            for i, c in enumerate(s):
                cnt[c] += 1
                # Key: differences between character counts
                k = (cnt["a"] - cnt["b"], cnt["b"] - cnt["c"])
                # If same key seen before, substring has equal counts
                if k in pos:
                    res = max(res, i - pos[k])
                else:
                    pos[k] = i
            return res

        # Check all three cases and return maximum
        x = singleChar(s)
        y = max(twoChars(s, "a", "b"), twoChars(s, "b", "c"), twoChars(s, "a", "c"))
        z = threeChars(s)
        return max(x, y, z)