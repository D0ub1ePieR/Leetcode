# 88、合并两个有序数组
> tag: python 、 数组 、 双指针

***
### 题目描述

&emsp;&emsp;给你两个有序整数数组 `nums1` 和 `nums2`，请你将 `nums2` 合并到 `nums1` 中，使 `num1` 成为一个有序数组。

### 说明

* 初始化 `nums1` 和 `nums2` 的元素数量分别为 `m` 和 `n` 。
* 你可以假设 `nums1` 有足够的空间（空间大小大于或等于 `m + n`）来保存 `nums2` 中的元素。

### 示例

```
  输入:
    nums1 = [1,2,3,0,0,0], m = 3
    nums2 = [2,5,6],       n = 3

  输出: [1,2,2,3,5,6]
```

***
### 题目链接
[88. 合并两个有序数组](https://leetcode-cn.com/problems/merge-sorted-array/)

***
### 题解

&emsp;&emsp;这里直接使用了 `bisect` 模块进行将 `nums2` 中的数插入至 `nums1` 中。预处理操作将 `nums1` 中所有的 `0` 删除。

```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        from bisect import insort
        for i in range(len(nums1)-m):
            del nums1[m]
        for i in nums2:
            insort(nums1, i)
```

&emsp;&emsp;最终结果，*运行时间44ms*，超过43.32%；*占用内存13.7MB*，超过5.36%。
