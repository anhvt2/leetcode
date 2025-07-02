# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Function to reverse the list from node `start` to `end`
        def reverse(start: ListNode, end: ListNode) -> ListNode:
            prev, curr = None, start
            while curr != end:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev
        
        # First, check if the list has at least `k` nodes
        count = 0
        ptr = head
        while ptr and count < k:
            ptr = ptr.next
            count += 1
            
        if count < k:
            return head  # If there are fewer than k nodes, return the original head

        # Reverse the first k nodes
        new_head = reverse(head, ptr)
        
        # `head` is now the tail of the reversed part, we need to connect it with the next segment
        head.next = self.reverseKGroup(ptr, k)
        
        return new_head
