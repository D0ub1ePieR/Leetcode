# 268、缺失数字
>tag: python 、 位运算 、 数组 、 数学

***
### 题目描述

&emsp;&emsp;给定一个包含 `0, 1, 2, ..., n` 中 `n` 个数的序列，找出 `0 .. n` 中没有出现在序列中的那个数。

### 示例1

```
  输入: [3,0,1]
  输出: 2
```

### 示例2

```
  输入: [9,6,4,2,3,5,7,0,1]
  输出: 8
```

**说明**：  
你的算法应具有线性时间复杂度。你能否仅使用额外常数空间来实现?

***
### 题目链接
[268.缺失数字](https://leetcode-cn.com/problems/missing-number/)

***
### 题解

* **一行 - 数学**

  很显然对 `0, .., n` 求和，随后减去给定数组的总和，即是缺少的一个数。

  ```python
  class Solution:
      def missingNumber(self, nums: List[int]) -> int:
          return len(nums)*(len(nums)+1)//2 - sum(nums)
  ```

* **一行 - 位运算**

  考虑到位运算中的 **与** 和 **或**，对于 `0, .., n` 中的多个数会出现恒为 `0/1` 的情况，那么就考虑用到异或操作，又异或对两个相同的数执行会得到 `0`，那么我们就可以首先将 `0, .., n` 这 `n+1` 个数进行异或操作，然后在将结果与数组中所有的数进行异或，最终剩下来的值便是缺少的那一个。

  ```python
  class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y:x^y, [i for i in range(len(nums)+1)]+nums)
  ```
