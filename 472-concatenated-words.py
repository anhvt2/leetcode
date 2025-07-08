class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        # Use a set for O(1) word lookup
        word_set = set(words)

        # Memoization dictionary to cache results for words we've already checked
        memo = {}

        # Helper function to determine if a word can be formed by concatenating other words in the set
        def canForm(word):
            # If we've already computed this word, return the cached result
            if word in memo:
                return memo[word]

            # Try every possible split of the word into prefix and suffix
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]

                # If the prefix is a word in the set,
                # and the suffix is either directly in the set or can be formed recursively
                if prefix in word_set:
                    if suffix in word_set or canForm(suffix):
                        memo[word] = True  # Cache and return True
                        return True

            memo[word] = False  # If no valid split found, cache and return False
            return False

        result = []

        # For each word in the list, check if it is a concatenated word
        for word in words:
            if not word:
                continue  # Skip empty strings

            # Temporarily remove the current word from the set to avoid using itself
            word_set.remove(word)

            # Check if it can
