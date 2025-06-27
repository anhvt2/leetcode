 # https://www.geeksforgeeks.org/given-linked-list-representation-of-complete-tree-convert-it-to-linked-representation/
# Python program to create a Complete Binary tree from its Linked List Representation

from collections import deque

class Lnode:
    def __init__(self, value):
        self.data = value
        self.next = None

class Tnode:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

# Converts a given linked list representing a complete binary tree into the linked representation of a binary tree.
def convert(head):
    if not head:
        return None
    # Queue to store the parent nodes
    q = deque()
    # The first node is always the root node, and add it to the queue
    root = Tnode(head.data)
    q.append(root)
    # Move the pointer to the next node
    head = head.next
    # Until the end of the linked list is reached, do the following steps
    while head:
        # Take the parent node from the queue and remove it from the queue
        parent = q.popleft()
        leftChild = None
        rightChild = None
        # Create left child
        if head:
            leftChild = Tnode(head.data)
            q.append(leftChild)
            head = head.next
        # Create right child
        if head:
            rightChild = Tnode(head.data)
            q.append(rightChild)
            head = head.next
        # Assign the left and right children of the parent
        parent.left = leftChild
        parent.right = rightChild
    return root

# Level Order Traversal of the binary tree
def levelOrderTraversal(root):
    if not root:
        return
    # Queue to hold nodes at each level
    q = deque()
    q.append(root)
    while q:
        currNode = q.popleft()
        # Print the current node's data
        print(currNode.data, end=" ")
        # Push the left and right children of the current node to the queue
        if currNode.left:
            q.append(currNode.left)
        if currNode.right:
            q.append(currNode.right)

if __name__ == "__main__":
  
    # Create linked list : 10->12->15->25->30->36
    head = Lnode(10)
    head.next = Lnode(12)
    head.next.next = Lnode(15)
    head.next.next.next = Lnode(25)
    head.next.next.next.next = Lnode(30)
    head.next.next.next.next.next = Lnode(36)
    
    root = convert(head)
    levelOrderTraversal(root)
