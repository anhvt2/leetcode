from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()
        current = dummy_head
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10

            current.next = ListNode(digit)
            current = current.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next
        #
        return dummy_head.next

# # Helper function to create a linked list from a list of list_numbers
# def build_list(list_numbers):
#     dummy = ListNode()
#     current = dummy
#     for n in list_numbers:
#         current.next = ListNode(n)
#         current = current.next
#     return dummy.next

# # Helper function to print a linked list as a list
# def print_list(node):
#     result = []
#     while node:
#         result.append(node.val)
#         node = node.next
#     print(result)

# l1 = build_list([2,4,3])
# l2 = build_list([5,6,4])
# sol = Solution()
# result = sol.addTwoNumbers(l1, l2)
# print_list(l1)
# print_list(l2)
# print_list(result)
