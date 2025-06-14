# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# from collections import deque
# Given the head of a singly linked list, return true if it is a Palindrome or false otherwise.

# O(n) space complexity, O(n) time complexity
# class Solution:
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         # lists = []
#         queue = deque()
#         headiter = head
#         while headiter is not None:
#             queue.append(headiter.val)
#             headiter = head.next
#         n = len(queue)
#         for i in range(n//2):
#             if queue[i] != queue[-i-1]:
#                 return False
#         return True

# Time complexity: O(n)
# Space complexity: O(1)

# Steps:
#     Find the middle of the linked list (slow/fast pointers).
#     Reverse the second half of the list.
#     Compare the first and second halves node by node.
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Step 1: Find middle (slow will point to middle)
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse second half
        prev = None
        curr = slow
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        
        # Step 3: Compare first and reversed second half
        first, second = head, prev
        while second:  # Only need to check the second half
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        return True
