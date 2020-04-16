# 442、数组中重复的数据
> tag: python3 、 数组

***
### 题目描述

&emsp;&emsp;给定一个整数数组 `a`，其中`1 ≤ a[i] ≤ n` （`n`为数组长度）, 其中有些元素出现**两次**而其他元素出现一次。

&emsp;&emsp;找到所有出现**两次**的元素。

&emsp;&emsp;你可以不用到任何额外空间并在`O(n)`时间复杂度内解决这个问题吗？

### 示例

```
  输入:
  [4,3,2,7,8,2,3,1]

  输出:
  [2,3]
```

***
### 题目链接
[442.数组中重复的数据](https://leetcode-cn.com/problems/find-all-duplicates-in-an-array/)

***
### 题解

&emsp;&emsp;与[找到所有数组中消失的数字](../448-Find_All_Numbers_Disappeared_in_an_Array-找到所有数组中消失的数字)类似的，要在 `O(n)` 的时间内且不用额外空间完成。那么我就可以通过遍历数组，遇到数字 `i` 则将 `nums[i-1]` 变为负数(因为出现的数字从一开始)，如果对应的位置的数已经为负数，那么说明该数出现了第二次。

```python
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for i in nums:
            if nums[abs(i)-1] < 0:
                res.append(abs(i))
            else:
                nums[abs(i)-1] *= -1
        return res
```

&emsp;&emsp;最终结果，*运行时间432ms*，超过83.74%；*占用内存21.2MB*，超过100.00%。
