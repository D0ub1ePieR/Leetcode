# python3
# medium
# 数组 二分查找
# 140ms 5.49%
# 31.1MB 5.11%

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        l1, l2 = len(matrix), len(matrix[0])
        start, end = 0, l1*l2-1
        while start <= end:
            mid = (start + end) // 2
            row = mid // l2
            col = mid - row * l2
            if matrix[row][col] == target:
                return True
            if matrix[row][col] < target:
                start = mid + 1
            else:
                end = mid - 1
        return False

# 152ms 5.23%
# 31.2MB 5.10%

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
        for i in range(len(matrix)-1):
            if matrix[i][0] <= target and matrix[i+1][0] > target:
                if target in matrix[i]:
                    return True
        if target in matrix[len(matrix)-1]:
            return True
        return False

# 220ms 5.01%
# 30.5MB 5.26%
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix == []:
            return False
        l = len(matrix)
        start, end = 0, l-1
        while start < end:
            mid = (start + end) // 2
            if matrix[mid][0] > target:
                end = mid - 1
            elif matrix[mid][0] < target:
                start = mid + 1
            else:
                return True
        if matrix[start] == []:
            return False
        if matrix[start][0] > target:
            index = start - 1
        else:
            index = start

        l = len(matrix[index])
        start, end = 0, l-1
        while start < end:
            mid = (start + end) // 2
            if matrix[index][mid] > target:
                end = mid - 1
            elif matrix[index][mid] < target:
                start = mid + 1
            else:
                return True
        if matrix[index][start] == target:
            return True
        return False
