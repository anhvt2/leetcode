# Python program for converting singly linked list
# into circular linked list.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function that converts singly linked list 
# into circular linked list
def circular(head): # O(n) time, O(1) space
    
    # declare a node variable curr and 
    # assign head node into curr node.
    curr = head
    
    # check that while curr->next is not equal
    # to NULL then curr points to next node.
    while curr.next is not None:
        curr = curr.next
    
    # assign curr->next to the head node.
    curr.next = head
    
    return head

# def circular(curr, head): # recursive - O(n) time, O(n) space
    
#     # if last node, then point next ptr
#     # to head Node
#     if curr.next == None:
#         curr.next = head
#         return
    
#     # otherwise move to the 
#     # next node
#     circular(curr.next, head)

def printList(head):
    curr = head
    
    while True:
        print(curr.data, end=" ")
        curr = curr.next
        if curr == head:
            break
    print()

if __name__ == "__main__":
    
    # create a hard coded list 10->12->14->16
    head = Node(10)
    head.next = Node(12)
    head.next.next = Node(14)
    head.next.next.next = Node(16)
    
    circular(head, head)
    
    printList(head)
