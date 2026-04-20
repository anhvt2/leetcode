class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # stack + set
        # 1. use a stack to track indices of unmatch '('
        # 2. if find an unmatched ')', record its index to remove later
        # 3. at the end, combine all unmatched indices in a set
        # 4. build a new string ignore characters at marked indices
        stack = []
        to_remove = set()

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop() # matched with a '('
                else:
                    to_remove.add(i) # unmatched ')'

        # any leftover '(' in stack is unmatched
        to_remove.update(stack)

        # reconstruct string without bad indices
        result = [c for i, c in enumerate(s) if i not in to_remove]
        return ''.join(result)