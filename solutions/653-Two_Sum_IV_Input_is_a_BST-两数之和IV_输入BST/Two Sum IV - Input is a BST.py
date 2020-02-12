# python3
# simple
# 树
# 80ms 90.45%
# 15.9MB 37.64%

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        d = set()
        self.flag = False
        def mid(node):
            if node.val in d:
                self.flag = True
                return
            else:
                d.add(k - node.val)
            if node.left:
                mid(node.left)
            if node.right:
                mid(node.right)

        mid(root)
        return self.flag
