# 41、缺失的第一个正数
> tag: python3 、 数组

***
### 题目描述

&emsp;&emsp;给你一个未排序的整数数组，请你找出其中没有出现的最小的正整数。

### 示例1

```
  输入: [1,2,0]
  输出: 3
```

### 示例2

```
  输入: [3,4,-1,1]
  输出: 2
```

### 示例3

```
  输入: [7,8,9,11,12]
  输出: 1
```

***
### 题目链接
[41.缺失的第一个正数](https://leetcode-cn.com/problems/first-missing-positive/)

***
### 题解

&emsp;&emsp;使用 `collections.Counter` 函数构造哈希表统计数组中各个数字出现的情况，输出第一个出现次数为零的数字。

```python
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        import collections
        t = collections.Counter(nums)
        i = 1
        while 1:
            if t[i] == 0:
                return i
            i += 1
```

&emsp;&emsp;最终结果，*运行时间36ms*，超过85.58%；*占用内存13.7MB*，超过16.67%。
