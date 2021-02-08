# Travesing Linked List : going through every single node, starting from head to tail (None)
class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None
    def __repr__(self):
        return self.data
    
class LinkedList():
    def __init__(self,nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for ele in nodes:
                node.next = Node(data=ele)
                node = node.next
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append('None')
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

# Create linked list with data and traverse through it

llist = LinkedList(['a','b','c','d'])
print(llist)

for node in llist:
    print(node)