class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # If the strings have different lengths, they cannot be isomorphic
        if len(s) != len(t):
            return False
        
        # Dictionaries to store the character mappings
        mapping_s_to_t = {}
        mapping_t_to_s = {}
        
        # Iterate through the characters of both strings
        for char_s, char_t in zip(s, t):
            # Check if char_s has been mapped to a different char_t
            if char_s in mapping_s_to_t:
                if mapping_s_to_t[char_s] != char_t:
                    return False
            else:
                mapping_s_to_t[char_s] = char_t
            
            # Check if char_t has been mapped to a different char_s
            if char_t in mapping_t_to_s:
                if mapping_t_to_s[char_t] != char_s:
                    return False
            else:
                mapping_t_to_s[char_t] = char_s
        
        return True
