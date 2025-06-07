from typing import List

# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         # Generate
#         ls = [""]
#         for i in range(n): # gradually insert "()" to every string in every possible way
#             tmp = []
#             for l in ls:
#                 if l == '': tmp += ["()"]
#                 for i in range(len(l)):
#                     tmp += [l[:i] + "()" + l[i:]]
#             ls = tmp
#         # Remove duplicates backward
#         for i, l in enumerate(ls):
#             # l = ls[i]
#             while l in ls:
#                 index = ls.index(l)
#                 del ls[index]
#             else:
#                 ls.append(l)
#         return ls

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(current: str, open_count: int, close_count: int):
            # open count: how many "("
            # close count: how many ")"
            if len(current) == 2 * n:
                result.append(current)
                return
            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)
            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return result



sol = Solution()
n = 4
result = sol.generateParenthesis(n)
print(result)
