class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')  # Remove all spaces
        num = 0
        stack = []
        sign = '+'  # Start with '+' to push the first number

        for i, ch in enumerate(s):
            if ch.isdigit():
                num = num * 10 + int(ch)

            # If current char is operator OR we're at the last character, process
            if not ch.isdigit() or i == len(s) - 1:
                if ch in '+-*/' or i == len(s) - 1:
                    if sign == '+':
                        stack.append(num)
                    elif sign == '-':
                        stack.append(-num)
                    elif sign == '*':
                        stack[-1] *= num
                    elif sign == '/':
                        # Use int() to truncate toward zero
                        stack[-1] = int(stack[-1] / num)

                    sign = ch  # Update current sign
                    num = 0    # Reset number

        return sum(stack)
