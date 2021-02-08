# Only information your linked list stoes is, the head of the linked list
class LinkedList():
    def __init__(self):
        self.head = None
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append('None')
        return " -> ".join(nodes)

# Create another class Node for representing each node of the linked list 
class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
    def __repr__(self):
        return self.data

# Creat a linked list
llist = LinkedList()
print(llist)
#Create a node 
first_node = Node('a')
# Make the node as head node
llist.head = first_node
print(llist)

#Adding more nodes to linked list
second_node = Node('b')
third_node = Node('c')
first_node.next = second_node
second_node.next = third_node
print(llist)
