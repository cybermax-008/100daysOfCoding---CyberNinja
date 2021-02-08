# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return isMirror(root,root)
def isMirror(L,R):
    if not L and not R:return True
    if L and R and L.val==R.val:
        return isMirror(L.right,R.left) and isMirror(L.left,R.right)
    return False