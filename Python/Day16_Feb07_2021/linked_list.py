from collections import deque

# deque is stands from double ended queue, this uses the implementation of linked list beneath.
# we can implement queue and stack using this module.

#Create empty linked list
my_llist = deque()
print(my_llist)

#Create a linked list with data. (Data should be iterable)
llist1 = deque([1,2,3,4,5])
print(llist1)
llist2 = deque(['a','b','c'])
print(llist2)
llist3 = deque('Hello world')
print(llist3)
llist4 = deque([{'name':'John'},{'age':23}])
print(llist4)

#Adding element to linked list - To the back
my_llist = deque('abcdef')
my_llist.append('g')
print(my_llist)

#Adding element to linked list - from front
my_llist = deque('abcdef')
my_llist.appendleft('z')
print(my_llist)

# Remove element from linked list - from back
my_llist.pop()
print(my_llist)
# Remove element from linked list - from left
my_llist.popleft()
print(my_llist)
