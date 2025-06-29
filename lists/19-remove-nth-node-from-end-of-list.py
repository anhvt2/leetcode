# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Get length
        l = 0
        curr = head
        while curr:
            curr = curr.next
            l += 1
        curr = head
        if l-n == 0:
            return head.next
        # remove n from end = remove (l-n+1) from start
        for i in range(l-n-1):
            curr = curr.next
        curr.next = curr.next.next
        return head

# class Solution: # two-pointer solution
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         # Create a dummy node to simplify edge cases such as removing the head
#         dummy = ListNode(0)
#         dummy.next = head
#         fast = slow = dummy
        
#         # Move the fast pointer n steps ahead
#         for _ in range(n):
#             fast = fast.next
        
#         # Move both slow and fast pointers until fast reaches the end
#         while fast.next:
#             slow = slow.next
#             fast = fast.next
        
#         # Now slow.next is the node to remove
#         slow.next = slow.next.next
        
#         return dummy.next  # Return the new head (in case the head was removed)

