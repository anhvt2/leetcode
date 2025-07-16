class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i1, i2, i = 0, 0, 0
        merge = ''
        while i1 < len(word1) and i2 < len(word2):
            if i % 2 == 0: # if even
                merge += word1[i1]
                i1 += 1
                i += 1
            else: # if odd
                merge += word2[i2]
                i2 += 1
                i += 1
        
        if i1 < len(word1):
            merge += word1[i1:]
        if i2 < len(word2):
            merge += word2[i2:]
        return merge
            
