# 74、搜索二维矩阵
> tag: python3 、 数组 、 二分查找

***
### 题目描述

&emsp;&emsp;编写一个高效的算法来判断 `m x n` 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

* 每行中的整数从左到右按升序排列。
* 每行的第一个整数大于前一行的最后一个整数。

### 示例1
```
  输入:
    matrix = [
      [1,   3,  5,  7],
      [10, 11, 16, 20],
      [23, 30, 34, 50]
    ]
  target = 3
  输出: true
```

### 示例2
```
  输入:
  matrix = [
    [1,   3,  5,  7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
  ]
  target = 13
  输出: false
```

***
### 题目链接
[74.搜索二维矩阵](https://leetcode-cn.com/problems/search-a-2d-matrix/)

***
### 题解
> 完整代码见 py文件。

> 该题最终超过的用户数量很低，可能因为测试用例发生过变动，导致现在提交类似或相同(哪怕复制完全相同的代码)算法都达不到统计时记录的执行用时。

* **逐行判断**

  &emsp;&emsp;对于 `matrix` 的行进行遍历，判断当前行的起始是否比 `target` 小，下一行的起始值是否比 `target` 大。如果满足则进行判断 `target` 是否位于本行，不满足则进入下一行。

  ```python
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
  ```
  &emsp;&emsp;最终结果，*运行时间152ms*，超过5.23%；*占用内存31.2MB*，超过5.10%。

* **行列二分法**

  &emsp;&emsp;首先对于行进行二分查找，找出 `target` 应该所处的行。随后对该行再次进行二分查找，判断 `target` 是否出现在当前行中。

  ```python
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
  ```
  &emsp;&emsp;最终结果，*运行时间220ms*，超过5.01%；*占用内存30.5MB*，超过5.26%。

* **整体二分法**

  &emsp;&emsp;将二维数组看做是一整个数组，计算出总的数字个数，对总个数进行二分查找，每一次通过坐标计算出其对应于二维数组的行和列值。

  ```python
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
  ```
  &emsp;&emsp;最终结果，*运行时间140ms*，超过5.49%；*占用内存31.1MB*，超过5.11%。
