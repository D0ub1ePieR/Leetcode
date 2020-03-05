# 18、四数之和
> tag: python3 、 数组 、 哈希表 、 双指针

***
### 题目描述

&emsp;&emsp;给定一个包含 `n` 个整数的数组 `nums` 和一个目标值 `target`，判断 nums 中是否存在四个元素 `a，b，c` 和 `d` ，使得 `a + b + c + d` 的值与 `target` 相等？找出所有满足条件且不重复的四元组。

### 注意
&emsp;&emsp;答案中不可以包含重复的四元组。

### 示例
```
  给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

  满足要求的四元组集合为：
  [
    [-1,  0, 0, 1],
    [-2, -1, 1, 2],
    [-2,  0, 0, 2]
  ]
```

***
### 题目链接
[18.四数之和](https://leetcode-cn.com/problems/4sum/)
***
### 题解

&emsp;&emsp;四数之和可以看做[三数之和](../15-3Sum-三数之和)之外再套一层循环，即最外层对数组进行遍历，随后在数组剩余部分使用三数之和的算法寻找和为剩余值的三个数。其中依旧进行了一些优化

  + 在每层循环初始进行判断，跳过与上一轮相同的值

  + 在每层循环中判断当前能达到的最大值和最小值，并与 `target` 比较。如果最大值比 `target` 小则可以跳过当前轮循环；如果最小值比 `target` 大，则可以直接跳出循环

  + 两个指针向中间移动过程中，跳过指针指向的相同的数

  ```python
    class Solution:
        def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
            nums.sort()
            l = len(nums)
            res = set()
            for i in range(l - 3):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                mid = target - nums[i]
                big_value = nums[i] + nums[l-1] + nums[l-2] + nums[l-3]
                small_value = nums[i] + nums[i+1] + nums[i+2] + nums[i+3]
                if big_value < target:
                    continue
                if small_value > target:
                    break
                for j in range(i + 1, l - 2):
                    if j > i + 1 and nums[j] == nums[j-1]:
                        continue
                    k = j + 1
                    n = l - 1
                    big_value = nums[j] + nums[n] + nums[n - 1]
                    small_value = nums[j] + nums[j + 1] + nums[j + 2]
                    if big_value < mid:
                        continue
                    if small_value > mid:
                        break
                    while k < n:
                        s = nums[j] + nums[k] + nums[n]
                        if s == mid:
                            res.add((nums[i], nums[j], nums[k], nums[n]))
                            n -= 1
                            while k < n and nums[n + 1] == nums[n]:
                                n -= 1
                            k += 1
                            while k < n and nums[k - 1] == nums[k]:
                                k += 1
                        elif s > mid:
                            n -= 1
                            while k < n and nums[n + 1] == nums[n]:
                                n -= 1
                        else:
                            k += 1
                            while k < n and nums[k - 1] == nums[k]:
                                k += 1
            return res
  ```
&emsp;&emsp;最终结果，*运行时间104ms*，超过87.45%；*占用内存13.2MB*，超过42.64%。
> 最终结果使用 集合 set 存储可以一定程度上提高运行速度，相比 列表 而言。
