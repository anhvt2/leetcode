class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken = set(brokenLetters)
        ans = 0
        for w in text.split():
            if all(ch not in broken for ch in w):
                ans += 1
        return ans

