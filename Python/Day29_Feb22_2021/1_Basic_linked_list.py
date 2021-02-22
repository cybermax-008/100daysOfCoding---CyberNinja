class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None

def print_l(head):
    curr_node = head
    while(curr_node):
        print(curr_node.data, end="->")
        curr_node=curr_node.next
    print(curr_node)


#Main program

llist = LinkedList() #empty linked list

llist.head = Node(2)
second = Node(3)
thrid = Node(5)

'''
Three nodes are created with references as head, second, and third.
'''
#Linking the Nodes using the references
llist.head.next = second
second.next = thrid

print_l(llist.head)
