# 1313、解压缩编码列表
>tag: python3 、 数组

***
### 题目描述

&emsp;&emsp;给你一个以行程长度编码压缩的整数列表 `nums` 。

&emsp;&emsp;考虑每对相邻的两个元素 `[freq, val] = [nums[2*i], nums[2*i+1]]` （其中 `i >= 0` ），每一对都表示解压后子列表中有 `freq` 个值为 `val` 的元素，你需要从左到右连接所有子列表以生成解压后的列表。

&emsp;&emsp;请你返回解压后的列表。

### 示例1

```
  输入：nums = [1,2,3,4]
  输出：[2,4,4,4]
  解释：第一对 [1,2] 代表着 2 的出现频次为 1，所以生成数组 [2]。
  第二对 [3,4] 代表着 4 的出现频次为 3，所以生成数组 [4,4,4]。
  最后将它们串联到一起 [2] + [4,4,4] = [2,4,4,4]。
```

### 示例2

```
  输入：nums = [1,1,2,3]
  输出：[1,3,3]
```

**提示**：
* `2 <= nums.length <= 100`
* `nums.length % 2 == 0`
* `1 <= nums[i] <= 100`

***
### 题目链接
[1313.解压缩编码列表](https://leetcode-cn.com/problems/decompress-run-length-encoded-list/)

***
### 题解

* **基础解法**

&emsp;&emsp;很基础的题目，首先将数组分为奇数项和偶数项两部分，随后将偶数项重复对应的奇数项次，组成最终的数组。

```python
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        x = nums[::2]
        y = nums[1::2]
        res = []
        for i in range(len(x)):
            res.extend([y[i] for _ in range(x[i])])
        return res
```

&emsp;&emsp;最终结果，*运行时间36ms*，超过94.63%；*占用内存13.7MB*，超过100.00%。这里考虑到 `eppend` 操作较为耗时，采用一次性追加数组的 `extend` 方式。

* **一行代码**

&emsp;&emsp;这类简单的题目自然少不了一行代码，一些列出了几种方式：

* 使用 `zip` 方式组合奇偶项

`return [i for i,j in zip(nums[1::2],nums[::2]) for _ in range(j)]`  

* 使用两层 `for` 循环

`return [nums[i] for i in range(len(nums)) for j in range(nums[i-1]) if i % 2 == 1]`

* 使用 `reduce` 函数配合 `lambda` 表达式

`return reduce(lambda x,y:x+y,[[nums[i+1]]*nums[i] for i in range(0,len(nums),2)])`

* 使用 `sum` 函数在数组类型上叠加

`return sum(([b] * a for a, b in zip(nums[::2], nums[1::2])), [])`

(部分来自论坛题解)
