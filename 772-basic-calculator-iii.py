class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        # a stack to store intermediate values
        # a recursive helper function to evaluate expression in side (...)
        # immediate evaluation of * and /
        # deferred + and - via stack
        def helper(it):
            stack = []
            num = 0
            sign = '+'

            while it: # order of the if blocks matters
                ch = it.pop(0)

                if ch.isdigit():
                    num = num * 10 + int(ch)
                
                if ch == '(':
                    num = helper(it)

                if not ch.isdigit() or not it:
                    if sign == '+':
                        stack.append(num)
                    elif sign == '-':
                        stack.append(-num)
                    elif sign == '*':
                        stack[-1] *= num
                    elif sign == '/':
                        stack[-1] = int(stack[-1] / num) # truncate toward zero

                    # reset
                    num = 0
                    sign = ch

                if ch == ')':
                    break         

            return sum(stack)
        return helper(list(s))