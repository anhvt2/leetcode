from typing import List
class Solution:
    def compress(self, chars: List[str]) -> int:
        l = 1 # length
        ptr = 0 # pointer
        curr = None # current char
        for c in chars:
            # Init
            if curr == None:
                curr = c
            # If repeat, then increase counter
            elif c == curr:
                l += 1
            elif c != curr:
                chars[ptr] = curr
                ptr += 1
                if l > 1:
                    for digit in str(l):
                        chars[ptr] = digit
                        ptr += 1
                # reset
                l = 1
                curr = c
        
        # save the last char
        chars[ptr] = curr
        ptr += 1
        if l > 1:
            for digit in str(l):
                chars[ptr] = digit
                ptr += 1
        return ptr
