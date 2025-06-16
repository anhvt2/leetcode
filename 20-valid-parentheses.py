# from collections import Counter

# class Solution:
#     def isValid(self, s: str) -> bool:
#         count = Counter(s)
#         # quick check
#         if (count['('] != count[')']) or (count['['] != count[']'])  or (count['{'] != count['}']):
#             return False
#         # LIFO principle
#         open_brackets = []
#         closed_brackets = []
#         for c in s:
#             if c in ['(', '[', '{']:
#                 open_brackets.append(c)
#             elif c in [')', ']', '}']:
#                 closed_brackets.append(c)
#                 if len(open_brackets)>0:
#                     cb = open_brackets.pop() # cb: closed bracket
#                     # check if 'c' and cb is a valid pair
#                     print(f'c = {c}, cb = {cb}')
#                     if (c==')' and cb=='(') or (c==']' and cb=='[') or (c=='}' and cb=='{'):
#                         continue
#                     else:
#                         return False
#                 else:
#                     return False
#         return True

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in bracket_map.values():
                stack.append(char)
            elif char in bracket_map:
                if not stack or stack[-1] != bracket_map[char]:
                    return False
                stack.pop()
            else:
                # Ignore non-bracket characters or raise error depending on constraints
                return False

        return len(stack) == 0

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Dictionary to match opening and closing brackets
        bracket_map = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in bracket_map.values():  # If it's an opening bracket
                stack.append(char)
            elif char in bracket_map:  # If it's a closing bracket
                # If the stack is empty or the top of the stack is not the matching opening bracket
                if not stack or stack.pop() != bracket_map[char]:
                    return False
        # If the stack is empty, all the brackets were properly matched
        return not stack


s = "()"
sol = Solution()
result = sol.isValid(s)
print(result)
