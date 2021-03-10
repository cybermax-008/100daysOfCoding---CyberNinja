class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        if not self.head:
            return True
        else:
            return False
    
    def enqueue(self,data):
        if not self.head:
            self.head = Node(data)
        else:
            curr_node = self.head
            while(curr_node.next):
                curr_node= curr_node.next
            new_node = Node(data)
            curr_node.next = new_node
            new_node.next = None


    def dequeue(self):
        if not self.head:
            print("the queue is empty")
        else:
            temp_node = self.head
            self.head = self.head.next
            value = temp_node.data
            del temp_node
            return value

    def __repr__(self):
        if self.isEmpty():
            print("the queue is empty")
        else:
            curr_node = self.head
            res = ''
            while(curr_node):
                res+=str(curr_node.data)+"->"
                curr_node = curr_node.next

            res+="NULL"
            return res

class Stack:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        if not self.head:
            return True
        else:
            return False

    def push(self,item):
        if self.isEmpty():
            self.head = Node(item)
        else:
            new_node = Node(item)
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.isEmpty():
            print("Stack is empty!")

        else:
            temp_node = self.head
            self.head = self.head.next
            value = temp_node.data
            del temp_node
            return value

    def __repr__(self):
        if self.isEmpty():
            print("the stack is empty")
        else:
            curr_node = self.head
            res = ''
            while(curr_node):
                res+=str(curr_node.data)+"->"
                curr_node = curr_node.next

            res+="NULL"
            return res


# Main program
my_stack = Stack()

# push some data
my_stack.push(2)
my_stack.push(4)
my_stack.push(7)
print(my_stack)

# pop some data
my_stack.pop()

print(my_stack)

my_queue = Queue()

#enqueue some data
my_queue.enqueue(2)
my_queue.enqueue(4)
my_queue.enqueue(7)

print(my_queue)

my_queue.dequeue()
my_queue.dequeue()

print(my_queue)
    