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

    def del_key(self,key):
        if not self.head:
            print("Linked list is empty!")
            return
        curr_node = self.head
        if self.head.data == key:
            self.head = curr_node.next
            curr_node = None
            return
        while(curr_node):
            if curr_node.data == key:
                break
            prev_node = curr_node
            curr_node = curr_node.next
        if curr_node == None:
            print("The given key is not available in the linked list!")
            return
        prev_node.next = curr_node.next
        curr_node = None


        


def print_l(head):
    curr_node = head
    while(curr_node):
        print(curr_node.data, end="->")
        curr_node=curr_node.next
    print(curr_node)



#Main program
llist = LinkedList()

llist.append(2)
llist.append(3)
llist.append(5)
llist.append(7)
llist.append(10)
print_l(llist.head)
llist.del_key_re(5)
print_l(llist.head)