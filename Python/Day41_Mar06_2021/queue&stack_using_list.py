class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self,item):
        if self.isEmpty():
            return None
        return self.items.pop()

    def size(self):
        return len(self.items)


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def pop(self):
        if self.isEmpty():
            return None
        return self.items.pop()

    def push(self,item):
        self.items.append(item)

    def size(self):
        return len(self.items)