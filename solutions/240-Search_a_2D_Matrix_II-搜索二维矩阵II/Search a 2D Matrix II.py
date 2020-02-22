# python3
# medium
# 二分查找 分治算法
# 44ms 55.65%
# 18.2MB 32.27%

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        row = len(matrix) - 1
        col = 0
        while col < len(matrix[0]) and row >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                row -= 1
            else:
                col += 1
        return False

# 52ms 28.53%
# 18.1MB 32.80%

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        for mat in matrix:
            if target in mat:
                return True
        return False
