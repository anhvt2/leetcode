# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Node:
    def __init__(self, newData):
        self.data = newData
        self.next = None

# https://www.geeksforgeeks.org/dsa/reverse-a-linked-list/

# Standard iterative reversal technique: O(1)
# The idea is to reverse the links of all nodes using three pointers: 
#     prev: pointer to keep track of the previous node
#     curr: pointer to keep track of the current node 
#     next: pointer to keep track of the next node

# Given the head of a list, reverse the list and return the
# head of reversed list

# Iterative method: O(n) time and O(1) space
# Follow the steps below to solve the problem:
# Initialize three pointers prev as NULL, curr as head, and next as NULL.
# Iterate through the linked list. In a loop, do the following:
#     Store the next node, next = curr -> next
#     Update the next pointer of curr to prev, curr -> next = prev
#     Update prev as curr and curr as next, prev = curr and curr = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Initialize three pointers: curr, prev and next
        prev = None
        curr = head

        # Traverse all the nodes of Linked List
        while curr is not None:
            # Store next
            next_node = curr.next

            # Reverse current node's next pointer
            curr.next = prev

            # Move pointers one position ahead
            prev = curr
            curr = next_node
        return prev


# Follow the steps below to solve the problem:
#     Divide the list in two parts - first node and rest of the linked list.
#     Call reverse for the rest of the linked list.
#     Link the rest linked list to first.
#     Fix head pointer to NULL.
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Recursion: O(n) time and O(n) space
        if head is None or head.next is None:
            return head

        # Reverse the rest of linked list and put the 
        # first element at the end
        rest = self.reverseList(head.next)

        # Make the current head as last node of 
        # remaining linked list
        head.next.next = head

        # Update next of current head to NULL
        head.next = None

        # Return the reversed linked list
        return rest

# # Using Stack - O(n) Time and O(n) Space
# Follow the steps below to solve the problem:

#     Push all the nodes(values and address) except the last node in the stack.
#     Once the nodes are pushed, update the Head pointer to the last node.
#     Start popping the nodes and push them at the end of the linked list in the same order until the stack is empty.
#     Update the next pointer of last node in the stack by NULL.
def reverseList(head):
    # Create a stack to store the nodes
    stack = []
    temp = head
    # Push all nodes except the last node into stack
    while temp.next is not None:
        stack.append(temp)
        temp = temp.next
  
    # Make the last node as new head of the linked list
    head = temp
  
    # Pop all the nodes and append to the linked list
    while stack:
        # append the top value of stack in list
        temp.next = stack.pop()
        # move to the next node in the list
        temp = temp.next
  
    # Update the next pointer of last node 
    # of stack to None
    temp.next = None
  
    return head


if __name__ == "__main__":

    # Create a hard-coded linked list:
    # 1 -> 2 -> 3 -> 4 -> 5
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Given Linked list:", end="")
    printList(head)

    head = reverseList(head)

    print("Reversed Linked List:", end="")
    printList(head)
