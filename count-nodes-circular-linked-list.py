# Python3 program to count number of 
# nodes in a circular linked list.

class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None

# Function to count nodes 
# in a given Circular linked list 
def countNodes(head):

    curr = head
    result = 0

    # return 0 for empty lists
    if (head == None) :
        return 0
    
    while True :
        curr = curr.next
        result = result + 1
        if (curr == head):
            break
    
    return result

if __name__=='__main__': 

    # create list: 1->2->3->4->5--->1
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = head

    print(countNodes(head))
