# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) ==1:
            root = TreeNode(nums.pop())
            return root
        elif len(nums) <3:
            root = TreeNode(nums[0])
            if nums[0]>=nums[1]:
                root.left = TreeNode(nums[1])
            else:
                root.right = TreeNode(nums[1])
            return root
                
        else:
            mid = len(nums)//2
            left = nums[:mid]
            right = nums[mid+1:]
            root = TreeNode(nums[mid])
            root.left =self.sortedArrayToBST(left)
            root.right =self.sortedArrayToBST(right)
            return root