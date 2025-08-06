class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        max_fruits = 0
        freq = defaultdict(int) # int -> frequency

        for right, fruit in enumerate(fruits):
            freq[fruit] += 1
            # If we have too many fruits, then shrink from the left
            while len(freq) > 2:
                freq[fruits[left]] -= 1
                if freq[fruits[left]] == 0:
                    del freq[fruits[left]]
                left += 1
            max_fruits = max(max_fruits, right - left + 1)

        return max_fruits
