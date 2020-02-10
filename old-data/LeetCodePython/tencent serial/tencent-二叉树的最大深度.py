# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deep(self,node):
        if node==None:
            return 0
        else:
            return max(self.deep(node.left)+1,self.deep(node.right)+1)
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.deep(root)
# 60.02
