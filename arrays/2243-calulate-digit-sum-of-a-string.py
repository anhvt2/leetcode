class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            tmp = []
            for i in range(0, len(s), k):
                tmp.append(s[i:i+k])
            for j, chunk in enumerate(tmp):
                tmp[j] = sum(int(x) for x in chunk)
            s = ''.join(str(num) for num in tmp)
        return s