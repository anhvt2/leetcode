class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_pal(l: int, r: int) -> bool:
            # check s[l..r] is a palindrome in O(r-l)
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                # try deleting s[l] or deleting s[r], but only once
                return is_pal(l + 1, r) or is_pal(l, r - 1)
            l += 1
            r -= 1
        return True
