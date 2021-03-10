class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        if not self.head:
            return "The linked list is empty!"
        res = ''
        curr_node = self.head
        while(curr_node):
            res+=str(curr_node.data)+"->"
            curr_node = curr_node.next
        res+="NULL"
        return res

    def insert_at_beginning(self,value):
        if not self.head:
            self.head = Node(value)
        else:
            new_node = Node(value,self.head)
            self.head = new_node
    def insert_at_ending(self,value):
        if not self.head:
            self.head = Node(value)
        else:
            curr_node = self.head
            while(curr_node.next):
                curr_node = curr_node.next
            curr_node.next = Node(value)
    def insert_after_value(self,data_after,data_to_insert):
        if not self.head:
            print("Linked list is empty!")
        else:
            if self.head.data == data_after:
                self.head.next = Node(data_to_insert,self.head.next)
            else:
                curr_node = self.head
                while(curr_node):
                    if curr_node.data == data_after:
                        curr_node.next = Node(value,curr_node.next)
                        break
                    curr_node = curr_node.next
    def get_length(self):
        count = 0
        curr_node = self.head
        while(curr_node):
            curr_node=curr_node.next
            count+=1
        return count

    def remove_by_value(self,data):
        if not self.head:
            print("the linked list is empty!")
        else:
            if self.head.data == data:
                temp_node = self.head
                self.head = self.head.next
                del temp_node
            else:
                curr_node = self.head
                while(curr_node.next):
                    if curr_node.next.data == data:
                        temp_node = curr_node.next
                        curr_node.next = curr_node.next.next
                        del temp_node
                        break

                    curr_node = curr_node.next

ll = LinkedList()

ll.insert_at_beginning("banana")
ll.insert_at_ending("mango")
ll.insert_at_ending("apple")
print(ll)
ll.remove_by_value("apple")
print(ll)


    
            
