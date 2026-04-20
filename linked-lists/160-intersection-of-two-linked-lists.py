# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# O(m+n) time complexity
# O(1) space complexity

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """
        If the two lists intersect, returns the first common node; otherwise None.
        """
        if not headA or not headB:
            return None

        a, b = headA, headB
        while a is not b:
            # Advance two pointers - when any reaches the end, then redirect to another linked list
            # If there is an intersection, a and b will meet after at most two passes
            a = a.next if a else headB
            b = b.next if b else headA
        
        return a # or b
