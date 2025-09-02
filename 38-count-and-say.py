class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 0:
            return ""   # edge case: no sequence when n == 0

        i = 1
        k = "1"         # the sequence starts with "1" at step 1

        # build sequence iteratively until we reach nth term
        while i < n:
            word = ""   # will hold the next sequence string
            prev = ""   # previous character while scanning current string
            count = 0   # count of consecutive occurrences of prev

            # scan through the current sequence string
            for ch in k:
                if ch == prev:
                    count += 1        # same as previous → increment run length
                else:
                    if prev:
                        # finish previous run: "count + prev digit"
                        word += str(count) + prev
                    # reset for new run
                    prev = ch
                    count = 1

            # after loop, flush the last run
            if prev:
                word += str(count) + prev

            # update for the next iteration
            k = word
            i += 1

        # when loop ends, k is the nth term of the sequence
        return k
