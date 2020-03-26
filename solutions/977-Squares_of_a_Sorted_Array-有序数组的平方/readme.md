# 977、有序数组的平方
> tag: python 、 数组 、 双指针

***
### 题目描述

&emsp;&emsp;给定一个按非递减顺序排序的整数数组 `A`，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。

### 示例1

```
  输入：[-4,-1,0,3,10]
  输出：[0,1,9,16,100]
```

### 示例2

```
  输入：[-7,-3,2,3,11]
  输出：[4,9,9,49,121]
```

### 提示

1. 1 <= A.length <= 10000
2. -10000 <= A[i] <= 10000
3. A 已按非递减顺序排序。

***
### 题目链接
[977. 有序数组的平方](https://leetcode-cn.com/problems/squares-of-a-sorted-array/)

***
### 题解

&emsp;&emsp;只需要一行就可以解决。很直观。

```python
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted([x**2 for x in A])
```

&emsp;&emsp;最终结果，*运行时间248ms*，超过82.29%；*占用内存15.7MB*，超过5.36%。
