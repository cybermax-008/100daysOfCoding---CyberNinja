class BinaryTree:
    def __init__(self,value):
        self.value = value
        self.left = self.right = None

    def insert_left(self,val):
        if not self.left:
            self.left = BinaryTree(val)
            return
        new_tree = BinaryTree(val)
        new_tree.left = self.left
        self.left = new_tree

    def insert_right(self,val):
        if not self.right:
            self.right = BinaryTree(val)
            return
        new_tree = BinaryTree(val)
        new_tree.right = self.right
        self.right = new_tree

    def pre_order(self):
        print(self.value)

        if self.left:
            self.left.pre_order()
        
        if self.right:
            self.right.pre_order()

    def in_order(self):
        if self.left:
            self.left.in_order()

        print(self.value)

        if self.right:
            self.right.in_order()

    def post_order(self):
        if self.left:
            self.left.post_order()
        if self.right:
            self.right.post_order()

        print(self.value)
            

    

a_node = BinaryTree('1')
a_node.insert_left('2')
a_node.insert_right('5')

b_node = a_node.left
b_node.insert_right('4')
b_node.insert_left('3')

c_node = a_node.right
c_node.insert_left('6')
c_node.insert_right('7')

d_node = b_node.right
e_node = c_node.left
f_node = c_node.right

print(a_node.in_order())



