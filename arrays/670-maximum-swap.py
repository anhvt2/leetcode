from typing import List

class Solution:
    def maximumSwap(self, num: int) -> int:
        s = list(str(num))
        # last[pos] = rightmost index of digit pos in s
        last = [-1] * 10
        # For each digit (left to right), if there is a larger digit later in the number, we should swap the current digit with the rightmost occurrence of that larger digit.

        for i, ch in enumerate(s): # 0 <= int(ch) <= 9, i alway increasing, so if two instances occur for the same digit, then select the larger one
            last[int(ch)] = i # last[d] = the last index where digit d appears in the number.

        # scan left->right, try to bring in a bigger digit from the right
        for i, ch in enumerate(s):
            cur = int(ch)
            for d in range(9, cur, -1):         # check bigger digits
                if last[d] > i:                  # a bigger digit exists to the right
                    j = last[d]
                    s[i], s[j] = s[j], s[i]
                    return int("".join(s))
        return num                                # already maximal
