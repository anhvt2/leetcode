class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def replaceVowel(word: str):
            return "".join(['*' if c in 'aeiou' else c for c in word])

        exact_words = set(wordlist)
        cap_map = {}
        vowel_map = {}

        for word in wordlist:
            lower = word.lower()
            if lower not in cap_map:
                cap_map[lower] = word
            
            vword = replaceVowel(lower)
            if vword not in vowel_map:
                vowel_map[vword] = word

        res = []

        for query in queries:
            if query in exact_words:
                res.append(query)
            elif query.lower() in cap_map:
                res.append(cap_map[query.lower()])
            elif replaceVowel(query.lower()) in vowel_map:
                res.append(vowel_map[replaceVowel(query.lower())])
            else:
                res.append("")
        
        return res