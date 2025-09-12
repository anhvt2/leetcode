class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = set("aeiouAEIOU")  # use AEIOU if input may be mixed case
        return any(c in vowels for c in s)
