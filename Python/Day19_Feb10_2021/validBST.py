Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Iterative solution
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack = [(root,-float('inf'),float('inf'))]
        
        while stack:
            root,lower,upper = stack.pop()
            if not root:
                continue
            val = root.val
            
            if val <= lower or val >= upper:
                return False
            
            stack.append((root.left,lower,val))
            stack.append((root.right,val,upper))
            
        return True

# Recursion solution
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def validate(node,lower=-float('inf'),upper=float('inf')):
            if not node:
                return True

            if node.val <= lower or node.val >= upper:
                return False
            return (validate(node.left,lower,node.val) and 
                    validate(node.right,node.val,upper))
        
        return validate(root)
            