# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        
        
        def isMirror(t1,t2):
            if not t1 and not t2:
                return True
            if t1 and t2:
                if t1.val == t2.val:
                    return isMirror(t1.left,t2.right) and isMirror(t1.right,t2.left)
                
        return isMirror(root,root)