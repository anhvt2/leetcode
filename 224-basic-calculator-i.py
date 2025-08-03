class Solution:
    def calculate(self, s: str) -> int:
        sign = 1
        res = 0 # accumulate partial res in ()
        stack = [] # handle multi level ()
        num = 0
        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch) # handle number greater than 9
            elif ch == "+":
                res += sign * num # add the number before +
                num = 0 # reset num for number greater than 9 handle
                sign = 1 # set the sign for the next num
            elif ch == "-":
                res += sign * num # add the number before -
                num = 0 # reset num for number greater than 9 handle
                sign = -1 # set the sign for the next num
            elif ch == "(":
                stack.append(res) # store the previous res/sign in stack before reset res
                stack.append(sign)
                sign = 1 # reset sign for new ()
                res = 0 # reset res because you need a fresh accumulator
            elif ch == ")":
                res += sign * num # early compute for the last num in ()
                num = 0 # reset num for number greater than 9 handle

                res *= stack.pop() # correct sign of res inside ()
                res += stack.pop() # reset res to be the sum of the num inside and outside the ()

            else: # ignore weird spaces
                continue
        return res + sign * num # handle the last num and one num case
        # 1+(4+5+2)-3
