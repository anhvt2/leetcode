class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq = {}
        # Count characters in string 's'
        for char in s:
            freq[char] = freq.get(char, 0) + 1

        result = []

        # Add characters in the specified 'order'
        for char in order:
            if char in freq:
                result += [char] * freq[char]
                del freq[char]

        # Add remaining char not in order
        for char, count in freq.items():
            result += [char] * count

        return ''.join(result)