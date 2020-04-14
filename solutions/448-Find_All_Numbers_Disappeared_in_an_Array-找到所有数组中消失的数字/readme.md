# 448、找到所有数组中消失的数字
>tag: python3 、 数组

***
### 题目描述

&emsp;&emsp;给定一个范围在  `1 ≤ a[i] ≤ n ( n = 数组大小 )` 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。

&emsp;&emsp;找到所有在 `[1, n]` 范围之间没有出现在数组中的数字。

&emsp;&emsp;您能在不使用额外空间且时间复杂度为`O(n)`的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。

### 示例

```
  输入:
  [4,3,2,7,8,2,3,1]

  输出:
  [5,6]
```

***
### 题目链接
[448.找到所有数组中消失的数字](https://leetcode-cn.com/problems/find-all-numbers-disappeared-in-an-array/)

***
### 题解

&emsp;&emsp;可以使用 `collections.Counter` 函数计算每个数出现的次数，也可以使用 `set` 函数将 `nums` 转变为集合，随后进行处理。

```python
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # import collections
        # return [i for i in range(1, len(nums)+1) if collections.Counter(nums)[i]==0]
        # return [i for i in range(1, len(nums)+1) if i not in nums]
        t = set(nums)
        return [i for i in range(1, len(nums)+1) if i not in t]
```

&emsp;&emsp;最终结果，*运行时间408ms*，超过86.94%；*占用内存23.1MB*，超过8.33%。这道题追求一行代码完成，由于需要中间结果每一次重复计算什么容易超时。
