class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)                # length of the string
        ans = 0                  # best length found so far

        # Consider each possible starting index i
        for i in range(n):
            cnt = [0] * 26       # frequency of each letter for substring [i..j]
            mx = 0               # maximum frequency seen in current substring
            distinct = 0         # how many distinct letters we've seen

            # Try all ending positions j ≥ i
            for j in range(i, n):
                c = ord(s[j]) - ord('a')   # map char to 0..25
                cnt[c] += 1

                # If this is the first time seeing this char in the substring
                if cnt[c] == 1:
                    distinct += 1         # increase distinct count

                # Update maximum frequency among characters seen so far
                if cnt[c] > mx:
                    mx = cnt[c]

                # A substring [i..j] is balanced if:
                #   max_freq * #distinct == length of substring
                # meaning each distinct char appears exactly mx times
                if mx * distinct == (j - i + 1):
                    # update answer if this balanced substring is longer
                    ans = max(ans, j - i + 1)

        return ans
