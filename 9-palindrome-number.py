class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        elif x==0:
            return True
        else:
            s = str(x)
            n = len(s)
            for i in range(n//2+1):
                if s[i] != s[n-1-i]:
                    return False
            else:
                return True

x = 1000021
sol = Solution()
print(sol.isPalindrome(x))
