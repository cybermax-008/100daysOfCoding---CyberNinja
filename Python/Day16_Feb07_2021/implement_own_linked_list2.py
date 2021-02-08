# linked list’s __init__() that allows you to quickly create linked lists with some data

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


# Create a linked list with data

llist = LinkedList(['a','b','c','d','e'])
print(llist)
                            