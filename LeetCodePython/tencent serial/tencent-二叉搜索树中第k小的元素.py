# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.res=[]
    def midsearch(self,node):
        if node.left:
            self.midsearch(node.left)
        self.res.append(node.val)
        if node.right:
            self.midsearch(node.right)
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.midsearch(root)
        return self.res[k-1]
# 52.99
