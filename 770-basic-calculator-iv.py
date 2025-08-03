from typing import List
from collections import Counter
import re

class Solution:
    def basicCalculatorIV(self, expression: str, evalvars: List[str], evalints: List[int]) -> List[str]:
        # build a map for substituted variables
        varmap = dict(zip(evalvars, evalints))
        # tokenize and reverse for easy pop from end
        tokens = re.findall(r'\d+|[a-z]+|[()+\-*]', expression)[::-1]

        def parse_expr() -> Counter:
            # parse a term, then any + or - that follow
            term = parse_term()
            while tokens and tokens[-1] in ('+', '-'):
                op = tokens.pop()
                right = parse_term()
                term = combine(term, right, op)
            return term

        def parse_term() -> Counter:
            # parse a factor, then any * that follow
            fact = parse_factor()
            while tokens and tokens[-1] == '*':
                tokens.pop()
                right = parse_factor()
                fact = combine(fact, right, '*')
            return fact

        def parse_factor() -> Counter:
            tok = tokens.pop()
            if tok == '(':
                expr = parse_expr()
                tokens.pop()  # discard ')'
                return expr
            if tok.isdigit():
                return Counter({(): int(tok)})
            if tok in varmap:
                return Counter({(): varmap[tok]})
            return Counter({(tok,): 1})

        def combine(c1: Counter, c2: Counter, op: str) -> Counter:
            res = Counter()
            if op == '+':
                # manual addition
                for k, v in c1.items(): res[k] += v
                for k, v in c2.items(): res[k] += v
            elif op == '-':
                # manual subtraction (preserves negatives)
                for k, v in c1.items(): res[k] += v
                for k, v in c2.items(): res[k] -= v
            else:  # op == '*'
                for k1, v1 in c1.items():
                    for k2, v2 in c2.items():
                        key = tuple(sorted(k1 + k2))
                        res[key] += v1 * v2
            return res

        # parse, filter zero coefficients, sort, and format
        result = parse_expr()
        result = {k: v for k, v in result.items() if v != 0}
        def sort_key(item):
            vars_, _ = item
            return (-len(vars_), vars_)
        sorted_items = sorted(result.items(), key=sort_key)

        output = []
        for vars_, coeff in sorted_items:
            if not vars_:
                output.append(str(coeff))
            else:
                output.append(f"{coeff}*{'*'.join(vars_)}")
        return output

# sol = Solution()
# expression = "e + 8 - a + 5"
# evalvars = ["e"]
# evalints = [1]
# res = sol.basicCalculatorIV(expression, evalvars, evalints)

# print(res)
# # outputs = ["14"]
# # expected = ["-1*a","14"]
