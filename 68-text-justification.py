from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        i, n = 0, len(words)

        while i < n:
            # 1) Greedily take as many words as fit
            line_len = len(words[i])
            j = i + 1
            while j < n and line_len + 1 + len(words[j]) <= maxWidth:
                line_len += 1 + len(words[j]) # 1 for space between words
                j += 1
            
            # words[i:j] are in this line
            k = j - i  # number of words
            is_last = (j == n)

            if k == 1 or is_last:
                # 2) Left-justify
                line = " ".join(words[i:j])
                line += " " * (maxWidth - len(line))
            else:
                # 3) Fully justify
                total_chars = sum(len(w) for w in words[i:j])
                spaces = maxWidth - total_chars
                gaps = k - 1
                base = spaces // gaps
                extra = spaces % gaps  # first 'extra' gaps get +1

                parts = []
                for t in range(gaps):
                    parts.append(words[i + t])
                    parts.append(" " * (base + (1 if t < extra else 0)))
                parts.append(words[j - 1])  # last word, no trailing spaces
                line = "".join(parts)

            res.append(line)
            i = j

        return res
