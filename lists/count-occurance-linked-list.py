# https://www.geeksforgeeks.org/dsa/write-a-function-that-counts-the-number-of-times-a-given-int-occurs-in-a-linked-list/

# Python program to count occurrences in
# a linked list by recursion
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Iterative: O(n) time, O(1) space
def count(head, key):
    curr = head
    count = 0
    while curr is not None:
        if curr.data == key:
            count += 1
        curr = curr.next
    return count

# Recursive: O(n) time, O(n) space
def count(head, key):
    if head is None:
        return 0
      
    ans = count(head.next, key)
    
    if head.data == key:
        ans += 1
    
    return ans

# Hard coded linked list: 
# 1 -> 2 -> 1 -> 2 -> 1
head = Node(1)
head.next = Node(2)
head.next.next = Node(1)
head.next.next.next = Node(2)
head.next.next.next.next = Node(1)

key = 1

print(count(head, key))
