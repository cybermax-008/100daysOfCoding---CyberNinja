# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution(object):
#     def levelOrder(self, root):
#         """
#         :type root: TreeNode
#         :rtype: List[List[int]]
#         """
#         level = [root]
#         res = []
#         while level:
#             curr_lvl_nodes = []
#             next_lvl_nodes = []
#             for node in level:
#                 curr_lvl_nodes.append(node.val)
#                 if node.left:
#                     next_lvl_nodes.append(node.left)
#                 if node.right:
#                     next_lvl_nodes.append(node.right)
                
#             res.append(curr_lvl_nodes)
#             level = next_lvl_nodes
            
#         return res
    
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        levels = []
        if not root:
            return levels
        level = 0
        level_buff = deque([root,])
        while level_buff:
            
            levels.append([])
            
            level_length = len(level_buff)
            
            for i in range(level_length):
                node = level_buff.popleft()
                levels[level].append(node.val)
                
                if node.left:
                    level_buff.append(node.left)
                if node.right:
                    level_buff.append(node.right)
            level+=1
            
        return levels