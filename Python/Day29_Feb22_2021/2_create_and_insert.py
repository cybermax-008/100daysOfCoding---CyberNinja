class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None

    def push(self,num):
        new_node = Node(num)
        if not self.head:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def append(self,num):
        new_node = Node(num)
        if not self.head:
            self.head = new_node
            return
        curr_node = self.head
        while(curr_node.next):
            curr_node=curr_node.next
        curr_node.next = new_node
    def insert_after(self,prev_node,num):
        if not prev_node:
            print("The given node is not present in linked list")
            return
        new_node = Node(num)
        new_node.next = prev_node.next
        prev_node.next = new_node

def print_l(head):
    curr_node = head
    while(curr_node):
        print(curr_node.data, end="->")
        curr_node=curr_node.next
    print(curr_node)



#Main program

llist = LinkedList() #empty linked list
# pushing to empty linked list
llist.push(2)
print_l(llist.head)

# pushing multiple nodes
llist.push(3)
llist.push(5)
llist.push(7)
print_l(llist.head)

llist_2 = LinkedList() #empty linked list

#appending to empty linked list
llist_2.append(2)
print_l(llist_2.head)

#appending multiple nodes 
llist_2.append(3)
llist_2.append(5)
llist_2.append(7)
print_l(llist_2.head)

#inset after
llist_2.insert_after(llist_2.head.next.next,10)
print_l(llist_2.head)