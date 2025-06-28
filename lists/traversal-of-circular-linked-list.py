# Python program to traverse a circular
# linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# recursive method: O(n) time, O(n) space
def print_list(curr, head):

    # return if list is empty
    if head is None:
        return
    
    print(curr.data, end=" ")
    
    if (curr.next == head):
        return
    
    print_list(curr.next, head)

# iterative method: O(n) time, O(1) space
def print_list(head):

    # return if list is empty
    if head is None:
        return

    curr = head
    while True:
        print(curr.data, end=" ")
        curr = curr.next
        if curr == head:
            break
    print()


if __name__ == "__main__":
  
    # Create a hard-coded linked list
    # 11 -> 2 -> 56 -> 12
    head = Node(11)
    head.next = Node(2)
    head.next.next = Node(56)
    head.next.next.next = Node(12)

    head.next.next.next.next = head

    print_list(head, head)