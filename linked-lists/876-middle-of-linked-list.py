# Given the head of a singly linked list, return the middle node of the linked list.

# If there are two middle nodes, return the second middle node.


from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Helper function to create a linked list from a list of list_numbers
def build_list(list_numbers):
    dummy = ListNode()
    current = dummy
    for n in list_numbers:
        current.next = ListNode(n)
        current = current.next
    return dummy.next

# Helper function to print a linked list as a list
def print_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    print(result)

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

# Alternative, more human, less memory-efficient
# class Solution:
#     def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         nodes = []
#         curr = head
#         while curr:
#             nodes.append(curr)
#             curr = curr.next
#         return nodes[len(nodes)//2]

# For odd-length lists, slow lands at the true middle.
# For even-length lists, slow lands at the second middle (which is what the problem wants).

test_lists = [1,2,3,4,5]
test_linked_list = build_list(test_lists)
sol = Solution()
result =  sol.middleNode(test_linked_list)
print(result)
