# 209、长度最小的子数组
> tag: python 、 数组 、 二分查找 、 双指针

***
### 题目描述

&emsp;&emsp;给定一个含有 `n` 个正整数的数组和一个正整数 `s` ，找出该数组中满足其和 `≥ s` 的长度最小的连续子数组。如果不存在符合条件的连续子数组，返回 `0`。

### 示例

```
  输入: s = 7, nums = [2,3,1,2,4,3]
  输出: 2
  解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。
```

### 进阶

如果你已经完成了 `O(n)` 时间复杂度的解法, 请尝试 `O(n log n)` 时间复杂度的解法。

***
### 题目链接
[209. 长度最小的子数组](https://leetcode-cn.com/problems/minimum-size-subarray-sum/)

***
### 题解

* **滑动窗口 + 双指针**

&emsp;&emsp;我们使用两个分别控制收尾的指针 `start, end` 来实现一个变长度的滑动窗口。这中间保证 **(1)** 每次 `end` 指针向后移动，直到第一次窗口内数的和大于 `s` ，**(2)** 随后 `start` 指针向后移动，直到第一次窗口内的数的和小于 `s`(这里首先移动至刚好大于 `s` 的位置，记录并比较最小值，随后再将 `start` 后移一次)。

* 例如 s = 7, nums = [2,3,1,2,4,3]

* 初始化， start = end = 0, min = len(nums) = 6

* start = 0, end = 3, [2, 3, 1, 2]

* start = 0, end = 3, min = 4,随后 start = start + 1 = 1

* start = 1, end = 4, [3, 1, 2, 4]

* start = 2, end = 4, min = 3,随后 start = 3

* start = 3, end = 5, [2, 4, 3]

* start = 4, end = 5, min = 2,随后 start = 5

```python
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        start = 0
        end = 0
        res = len(nums)
        if sum(nums) < s:
            return 0
        while end < len(nums):
            while sum(nums[start:end]) < s and end < len(nums):
                end += 1
            while end - start > 1 and sum(nums[start+1:end]) >= s:
                start += 1
            res = min(res, end-start)
            start += 1
        return res
```

&emsp;&emsp;最终结果，*运行时间2812ms*，超过5.02%；*占用内存15.2MB*，超过82.76%。发现结果效率十分的低，仔细一考虑发现，每次都要对数组切片并求和，是一个很耗时的操作。那么我们就可以引入一个变量来存储当前窗口内数的和。

```python
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        start = 0
        end = 0
        res = len(nums)
        if sum(nums) < s:
            return 0
        temp_sum = 0
        while end < len(nums):
            while temp_sum < s and end < len(nums):
                temp_sum += nums[end]
                end += 1
            while end - start > 1 and temp_sum - nums[start] >= s:
                temp_sum -= nums[start]
                start += 1
            res = min(res, end-start)
            temp_sum -= nums[start]
            start += 1
        return res
```

&emsp;&emsp;最终结果，*运行时间56ms*，超过86.32%；*占用内存15.2MB*，超过90.95%。效率得到了很大幅度的提升。
