# https://www.geeksforgeeks.org/dsa/write-a-c-function-to-print-the-middle-of-the-linked-list/
# Java program to illustrate how to find the middle element
# by counting the number of nodes

class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

# Helper function to find length of linked list
def getLength(head):

    # Variable to store length
    length = 0

    # Traverse the entire linked list and increment length
    # by 1 for each node
    while head:
        length += 1
        head = head.next

    # Return the number of nodes in the linked list
    return length

# Function to find the middle element of the linked list
# Iterative method: O(n) time, O(1) space
def getMiddle(head):

    # Finding length of the linked list
    length = getLength(head)

    # Traverse till we reach half of the length
    mid_index = length // 2
    while mid_index:
        head = head.next
        mid_index -= 1

    # Head now will be pointing to the middle element
    return head.data

# Tortoise and hare algorithm
def getMiddle(head):

    # Initialize the slow and fast pointer to the
    # head of the linked list
    slow_ptr = head
    fast_ptr = head

    while fast_ptr is not None and fast_ptr.next is not None:

        # Move the fast pointer by two nodes
        fast_ptr = fast_ptr.next.next

        # Move the slow pointer by one node
        slow_ptr = slow_ptr.next

    # Return the slow pointer which is currently pointing to the
    # middle node of the linked list
    return slow_ptr.data


def main():

    # Create a hard-coded linked list:
    # 10 -> 20 -> 30 -> 40 -> 50 -> 60
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)
    head.next.next.next.next = Node(50)
    head.next.next.next.next.next = Node(60)

    print(getMiddle(head))

if __name__ == "__main__":
    main()