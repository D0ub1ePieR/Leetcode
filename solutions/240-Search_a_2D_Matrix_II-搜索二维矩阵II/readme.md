# 240、搜索二维矩阵 II
> tag: python 、 二分查找 、 分治算法

***
### 题目描述

&emsp;&emsp;编写一个高效的算法来搜索 `m x n` 矩阵 `matrix` 中的一个目标值 `target`。该矩阵具有以下特性：

* 每行的元素从左到右升序排列。

* 每列的元素从上到下升序排列。

### 示例

&emsp;&emsp;现有矩阵 `matrix` 如下：
```
  [
    [1,   4,  7, 11, 15],
    [2,   5,  8, 12, 19],
    [3,   6,  9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
  ]
```
&emsp;&emsp;给定 `target = 5` ，返回 `true`.  

&emsp;&emsp;给定 `target = 20` ，返回 `false`.

***
### 题目链接
[240. 搜索二维矩阵 II](https://leetcode-cn.com/problems/search-a-2d-matrix-ii/)
***
# 题解

* **暴力法**

&emsp;&emsp;最简单的想到便是遍历每一行，判断 `target` 是否在该行内。

```python
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
```
  &emsp;&emsp;最终结果，*运行时间52ms*，超过28.53%；*占用内存18.1MB*，超过32.80%。

  > 后来发现这里第一个判断可以忽略，如果 matrix 为 [[]] 或 []也会返回正确的值，并且最终结果会变得不逊色于其他的算法。更离谱的是，最终统计结果记录的透明就是有这个方法所占据着。

* **搜索空间缩减**

  &emsp;&emsp;由于输入 `matrix` 的特性，我们可以发现如果 `target` 比其中一个数大，那么这个数的左上角部分则不可能出现 `target`；如果比其中一个数小，那么这个数的右下角部分则不可能出现 `target`。那么我们就可以利用这个特性，沿着数组中间列进行比较，并将数组分为四个区域(`左上、右上、左下、右下`)，其中 `target` 只可能出现在 **左下和右上** 部分。

  &emsp;&emsp;那么沿着数组中间列找到比上一个元素大，比下一个元素小的位置，就可以将 `matrix` 分为四部分，取其中两部分再进行同样的操作(递归)。最终能找到 `target` 则返回 `True`，否则返回 `False`。

* **行列双指针**

  &emsp;&emsp;考虑到 `matrix` 中，从左往右数字必定变大，从下往上数字必定变小(*为了使变大或变小只有一个方向走，所以不去从下往上。同样的取从右上角向左下角方向移动也是可以的*)，那么我们就可以将初始指针固定在数组的左下角，随后与 `target` 进行比较，如果指向的数比 `target` 大则将行指针向上移动一格，如果指向的数比 `target` 小则将列指针向右移动一格，否则相等直接返回 `True`。

  ```python
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
  ```

  &emsp;&emsp;最终结果，*运行时间44ms*，超过55.60%；*占用内存18.2MB*，超过32.27%。
