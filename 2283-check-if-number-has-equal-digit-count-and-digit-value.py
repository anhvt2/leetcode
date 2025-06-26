from collections import Counter
class Solution:
    def digitCount(self, num: str) -> bool:
        count = Counter(num)
        for i in range(len(num)):
            if int(num[i]) != count[str(i)]:
                return False
        return True
