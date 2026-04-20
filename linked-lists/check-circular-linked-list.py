# Python program to check if linked list is circular
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to check if the linked list is circular
def is_circular(head):
    # If head is null, list is empty, circular
    if not head:
        return True

    temp = head

    # Traverse until the end is reached or
    # the next node equals the head
    while head and head.next != temp:
        head = head.next

    # If end reached before finding head again, list is not circular
    if not head or not head.next:
        return False

    # If head found again, list is circular
    return True

# The idea is to use two pointers, slow and fast, to traverse the linked list. The slow pointer moves one step at a time, while the fast pointer moves two steps at a time. If the list is circular, the fast pointer will eventually meet the slow pointer; otherwise, the fast pointer will reach NULL indicating the list is not circular.
# O(n) time and O(1) space
# def is_circular(head):
#     if not head:
#         return True

#     slow = head
#     fast = head.next
#     while fast and fast.next:
#         if slow == fast:
#             return True
#         slow = slow.next
#         fast = fast.next.next

#     return False


if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)

    # Check if the linked list is circular
    print("Yes" if is_circular(head) else "No")

    # Making the linked list circular
    head.next.next.next.next = head

    # Check again if the linked list is circular
    print("Yes" if is_circular(head) else "No")
