class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # Stack (index sentinel)
        # For each i:
        #   if s[i] == '(', push i
        #   else pop, if stack becomes empty, push i (new base). otherwise, update max with (i - stack[-1])
        # time: O(n), space O(n)
        stack = [-1] # sentinel index base
        best = 0
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i) # reset base after an unmatched ')'
                else:
                    best = max(best, i - stack[-1])
        return best