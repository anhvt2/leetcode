class Solution:
    def applySubstitutions(self, replacements: List[List[str]], text: str) -> str:
        replacement_dict = {}
        for replace_char, replace_text in replacements:
            replacement_dict[replace_char] = replace_text
        
        while "%" in text:
            chunks = text.split("%")
            new_text = ""
            for chunk in chunks:
                if chunk in replacement_dict:
                    new_text += replacement_dict[chunk]
                else:
                    new_text += chunk
            
            text = new_text
        
        return text