# You are given the head of a linked list with n nodes.
# For each node in the list, find the value of the next greater node. That is, for each node, find the value of the first node that is next to it and has a strictly larger value than it.
# Return an integer array answer where answer[i] is the value of the next greater node of the ith node (1-indexed). If the ith node does not have a next greater node, set answer[i] = 0.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# How do we achieve this efficiently?
#     We use a stack to keep track of indices whose next greater value we haven’t found yet.
#     As we scan the array from left to right:
#         When we find a value greater than the value at the index on top of the stack, we have found the next greater node for that index.

# Key Points:
#     The stack always contains indices of nodes for which we are looking for the next greater value.
#     The values in the stack are always in decreasing order from bottom to top.
#     As soon as a larger value is found, we pop from the stack and set that index in the answer array.

# O(n) time and O(n) space
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        # Step 1: Convert linked list to array
        values = []
        while head:
            values.append(head.val)
            head = head.next

        answer = [0] * len(values)
        stack = []  # Stack of indices

        # Step 2: Monotonic stack
        # stack continuously pops until the last value of stack more than val, i.e. values[stack[-1]] > val
        for i, val in enumerate(values):
            while stack and values[stack[-1]] < val:
                answer[stack.pop()] = val
            stack.append(i)

        return answer

