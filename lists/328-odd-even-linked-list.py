# Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.
# The first node is considered odd, and the second node is even, and so on.
# Note that the relative order inside both the even and odd groups should remain as it was in the input.
# You must solve the problem in O(1) extra space complexity and O(n) time complexity.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Approach
#     Use two pointers:
#     odd: for the last node in the odd-indexed list
#     even: for the last node in the even-indexed list
#     even_head: to remember the head of the even-indexed list (so you can link it after all the odd nodes)
#     Walk through the list, rewiring next pointers so that:
#     All odd nodes are linked together
#     All even nodes are linked together
#     Link the odd list to the even list at the end.

# class Solution:
#     def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         # Edge case: if list is empty or has only one node, just return as is
#         if not head or not head.next:
#             return head

#         # odd: pointer to last node in odd list (starts at head)
#         # even: pointer to last node in even list (starts at head.next)
#         # even_head: keeps the start of the even-indexed nodes for final concatenation
#         odd = head
#         even = head.next
#         even_head = even

#         # Traverse the list, rewiring pointers
#         while even and even.next:
#             # Link current odd node to the next odd node
#             odd.next = even.next
#             odd = odd.next        # Move odd pointer forward

#             # Link current even node to the next even node
#             even.next = odd.next
#             even = even.next      # Move even pointer forward

#         # At end, link last odd node to the head of even nodes
#         odd.next = even_head
#         return head

# Two-pass solutions: pass through with the odd first, keep the first even index to attach odd and even
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        odd = head             # The head of the odd-indexed nodes
        even = head.next       # The head of the even-indexed nodes
        even_head = even       # Save start of even list to attach later

        # Loop through the list, separating odds and evens
        while even and even.next:
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next

        # Attach even list after odd list
        odd.next = even_head
        return head


# Input: head = [1,2,3,4,5]
# Output: [1,3,5,2,4]
