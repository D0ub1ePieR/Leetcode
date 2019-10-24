# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findcommon(self,node,p,q):
        if node==None:
            return None
        if node==p or node==q:
            return node
        left=self.findcommon(node.left,p,q)
        right=self.findcommon(node.right,p,q)
        if left and right:
            return node
        elif left:
            return left
        elif right:
            return right
        else:
            return None
    
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        return self.findcommon(root,p,q)
# 96.77
