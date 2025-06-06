class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()         # Store unique characters in the current window
        left = 0             # Left boundary of the window
        max_len = 0          # Tracks the maximum length found

        # Expand the window one character at a time from the right
        for right in range(len(s)):
            # If current character is already in the set, shrink window from the left
            while s[right] in seen:
                seen.remove(s[left])  # Remove leftmost character from the set
                left += 1             # Move left pointer right to reduce window size

            # Add the current character to the set
            seen.add(s[right])

            # Update max length if current window is larger
            max_len = max(max_len, right - left + 1)

        return max_len

s = "pwwkew"
sol = Solution()
result = sol.lengthOfLongestSubstring(s)
print(result)
