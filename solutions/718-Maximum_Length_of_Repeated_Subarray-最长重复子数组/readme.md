# 718、最长重复子数组
> tag: python 、 数组 、 哈希表 、 二分查找 、 动态规划

***
### 题目描述

&emsp;&emsp;给两个整数数组 `A` 和 `B` ，返回两个数组中公共的、长度最长的子数组的长度。

### 示例

```
  输入:
    A: [1,2,3,2,1]
    B: [3,2,1,4,7]
  输出: 3
  解释:
    长度最长的公共子数组是 [3, 2, 1]。
```

### 说明

1. 1 <= len(A), len(B) <= 1000
2. 0 <= A[i], B[i] < 100

***
### 题目链接
[718. 最长重复子数组](https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray/)

***
### 题解

* **动态规划**

&emsp;&emsp;构造一个大小为 `(len(A)+1) * (len(B)+1)` 的矩阵 `dp`，初始化为0,。最后一列及最后一行，用于存储数组最后一个数比较的转移状态。数组中第 `i` 行第 `j` 列存储了 `A[i:]` 与 `B[j;]` 的最长公共子串长度。

  - 当 `A[i] == B[j]` 时，`dp[i][j] = d[i+1][j+1] + 1`，即后一位的最长子串长度加一

  - 当 `A[i] != B[j]` 时，`dp[i][j] = 0` 保持为零

```python
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        dp = [[0] * (len(B) + 1) for i in range(len(A) + 1)]
        for i in range(len(A)-1, -1, -1):
            for j in range(len(B)-1, -1, -1):
                if A[i] == B[j]:
                    dp[i][j] = dp[i+1][j+1] + 1
        return max(max(row) for row in dp)
```

&emsp;&emsp;最终结果，*运行时间2996ms*，超过88.42%；*占用内存39.1MB*，超过6.00%。

> 这里初始化 dp 数组时，最外层不能再使用 * 操作。会导致每一行都是第一行的复制，这里会导致每一行的地址是相同的。

> 最后取 dp 最大值时，不能使用 max(max(dp)) ，会导致判断最大行时，按照下标顺序比较大小。
