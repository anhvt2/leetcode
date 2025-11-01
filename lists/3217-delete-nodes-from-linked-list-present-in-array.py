# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        # Convert list to set for efficiency
        set_nums = set(nums)

        # Create dummy node to handle edge case
        dummy = ListNode()
        dummy.next = head

        # Traverse and remove nodes
        prev = dummy
        current = head
        while current:
            if current.val in set_nums: # Skip this node
                prev.next = current.next
            else: # Move prev pointer if didn't delete
                prev = current
            current = current.next
        
        return dummy.next
