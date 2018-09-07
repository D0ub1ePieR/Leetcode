# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.maxnum=0
    def findmax(self,node):
        if node.left==None and node.right==None:
            self.maxnum=max(self.maxnum,node.val)
            return node.val
        if node.left and node.right==None:
            left=self.findmax(node.left)
            if left<0:
                self.maxnum=max(self.maxnum,node.val)
                return node.val
            else:
                self.maxnum=max(self.maxnum,node.val+left)
                return node.val+left
        if node.left==None and node.right:
            right=self.findmax(node.right)
            if right<0:
                self.maxnum=max(self.maxnum,node.val)
                return node.val
            else:
                self.maxnum=max(self.maxnum,node.val+right)
                return node.val+right
        if node.left and node.right:
            left=self.findmax(node.left)
            right=self.findmax(node.right)
            if left<0 and right<0:
                self.maxnum=max(self.maxnum,node.val)
                return node.val
            if left<0:
                self.maxnum=max(self.maxnum,node.val+right)
                return node.val+right
            if right<0:
                self.maxnum=max(self.maxnum,node.val+left)
                return node.val+left
            else:
                self.maxnum=max(self.maxnum,node.val+right+left)
                return max(node.val+left,node.val+right)
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxnum=root.val
        self.findmax(root)
        return self.maxnum
# 32.43
        
