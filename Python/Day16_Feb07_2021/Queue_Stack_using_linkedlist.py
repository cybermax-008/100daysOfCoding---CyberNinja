from collections import deque

# Implementing Queue and Stack using linked list

#QUEUE - FIFO : Add elelments to the back and Remove elements from the left
print("Implementation of Queue.....")
my_queue = deque()

# Add element to the queue
my_queue.append('a')
print(my_queue)
my_queue.append('b')
print(my_queue)
my_queue.append('c')
print(my_queue)
my_queue.append('d')
print(my_queue)
my_queue.append('e')
print(my_queue)

#Remove element from the queue (FIFO)
my_queue.popleft()
print(my_queue)
my_queue.popleft()
print(my_queue)
my_queue.popleft()
print(my_queue)

#STACK - LIFO : Add elelments on top and Remove elements from top
print("Implementation of Stack")
my_stack = deque()

# Add elments to the stack
my_stack.appendleft('a')
print(my_stack)
my_stack.appendleft('b')
print(my_stack)
my_stack.appendleft('c')
print(my_stack)
my_stack.appendleft('d')
print(my_stack)
my_stack.appendleft('e')
print(my_stack)

#Remove elements from the Stack (LIFO)
my_stack.popleft()
print(my_stack)
my_stack.popleft()
print(my_stack)
my_stack.popleft()
print(my_stack)
my_stack.popleft()
print(my_stack)
my_stack.popleft()
print(my_stack)