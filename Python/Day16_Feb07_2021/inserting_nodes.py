# Insertion of nodes : begining, ending and in between
class Node:
    # Create a node with data and pointer to next element
    def __init__(self,data):
        self.data = data 
        self.next = None
    # for representing node
    def __repr__(self):
        return self.data
    
class LinkedList():
    # Create a Linked list with data
    def __init__(self,nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for ele in nodes:
                node.next = Node(data=ele)
                node = node.next
    # for representaion
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append('None')
        return " -> ".join(nodes)
    # For Traversing 
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
    # inserting at first
    def add_first(self,node):
        node.next = self.head
        self.head = node

    # inserting at end
    def add_last(self,node):
        if not self.head:
            self.head = Node
        for current_node in self:
            pass
        current_node.next = node