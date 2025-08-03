from typing import List
class Solution:
    def compress(self, chars: List[str]) -> int:
        len = 1
        ptr = 0 # pointer
        curr = None
        for c in chars:
            # Init
            if curr == None:
                curr = c
            # If repeat, then increase counter
            elif c == curr:
                len += 1
            elif c != curr:
                chars[ptr] = curr
                ptr += 1
                if len > 1:
                    for digit in str(len):
                        chars[ptr] = digit
                        ptr += 1
                # reset
                len = 1
                curr = c
        
        # save the last char
        chars[ptr] = curr
        ptr += 1
        if len > 1:
            for digit in str(len):
                chars[ptr] = digit
                ptr += 1
        return ptr
