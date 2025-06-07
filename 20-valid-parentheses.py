from collections import Counter

class Solution:
    def isValid(self, s: str) -> bool:
        count = Counter(s)
        # quick check
        if (count['('] != count[')']) or (count['['] != count[']'])  or (count['{'] != count['}']):
            return False
        # LIFO principle
        open_brackets = []
        closed_brackets = []
        for c in s:
            if c in ['(', '[', '{']:
                open_brackets.append(c)
            elif c in [')', ']', '}']:
                closed_brackets.append(c)
                if len(open_brackets)>0:
                    cb = open_brackets.pop() # cb: closed bracket
                    # check if 'c' and cb is a valid pair
                    print(f'c = {c}, cb = {cb}')
                    if (c==')' and cb=='(') or (c==']' and cb=='[') or (c=='}' and cb=='{'):
                        continue
                    else:
                        return False
                else:
                    return False
        return True

s = "()"
sol = Solution()
result = sol.isValid(s)
print(result)
