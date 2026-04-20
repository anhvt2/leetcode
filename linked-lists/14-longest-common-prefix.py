class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]
        else:
            # longest possible prefix = minimum length of string in the bag
            min_len = float('inf')
            for i, string in enumerate(strs):
                min_len = min(min_len, len(string))

            prefix = ""
            for i in range(min_len):
                candidate_char = strs[0][i]
                for j, string in enumerate(strs):
                    if string[i] != candidate_char:
                        return prefix
                prefix += candidate_char
            return prefix