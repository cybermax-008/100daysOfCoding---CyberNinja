# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        lower= -float('inf')
        upper = float('inf')
        stack = [(root,lower,upper)]
        
        while stack:
            root,lower,upper = stack.pop()
            if not root:
                continue
            curr_val = root.val
            if curr_val <= lower or curr_val >= upper:
                return False
            stack.append((root.right,curr_val,upper))
            stack.append((root.left,lower,curr_val))
        return True