class Solution:
    def isValid(self, word: str) -> bool:
        word = word.lower()
        if len(word) < 3 or not word.isalnum():
            return False

        vowels = set("aeiou")
        has_vowel = any(c in vowels for c in word)
        has_consonant = any(c.isalpha() and c not in vowels for c in word)

        return has_vowel and has_consonant
