from typing import List, Optional

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Idea: 
        # (1) Convert linked-lists to simple list
        # (2) Sort
        # (3) Convert simple list to a linked list
        # Flatten linked-lists to simple list
        nodes = []
        for l in lists:
            while l:
                nodes.append(l.val)
                l = l.next
        # Sort
        nodes.sort()
        # Convert simple lists to a linked list
        dummy_head = root = ListNode()
        for node in nodes:
            root.next = ListNode(node)
            root = root.next
        return dummy_head.next
