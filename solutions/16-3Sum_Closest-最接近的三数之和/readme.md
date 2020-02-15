# 16、最接近的三数之和
> tag: python3 、 数组 、 双指针

***
### 题目描述
&emsp;&emsp;给定一个包括 `n` 个整数的数组 `nums` 和 一个目标值 `target`。找出 `nums` 中的三个整数，使得它们的和与 `target` 最接近。返回这三个数的和。假定每组输入只存在**唯一**答案。

### 示例
```
  例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.

  与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
```
***
### 题目链接
[16.最接近的三数之和](https://leetcode-cn.com/problems/3sum-closest/)
***
### 题解
* **双指针**

  &emsp;&emsp;使用和[三数之和](..\solutions\15-3Sum-三数之和)一样的双指针解法，只是目标从寻找和为零变为了每次比较和与 `target` 之间的差。在比较时需要考虑
  + 三数的和已经等于 `target`，那么就可以直接返回 `target` ，不会有更接近的值产生

  + 三数的和与 `target` 的差比当前最优的值与 `target` 的差更小，则更新记录值

  + 三数的和大于 `target` ，则将右边的指针向左移动直到出现下一个值与当前指向的值不同

  + 三数的和小于 `target` ，则将左边的指针向右移动直到出现下一个值与当前指向的值不同

  ```python
  class Solution:
      def threeSumClosest(self, nums: List[int], target: int) -> int:
          nums.sort()
          res = nums[0] + nums[1] + nums[2]
          for i in range(len(nums)):
              j = i + 1
              k = len(nums) - 1
              while j < k:
                  s = nums[i] + nums[j] + nums[k]
                  if s == target:
                      return s
                  elif abs(s - target) < abs(res - target):
                      res = s
                      # 可以和并入下方的指针移动
                      if s > target:
                          k -= 1
                          while j < k and nums[k + 1] == nums[k]:
                              k -= 1
                      else:
                          j += 1
                          while j < k and nums[j] == nums[j - 1]:
                              j += 1
                      #
                  elif s > target:
                      k -= 1
                      while j < k and nums[k + 1] == nums[k]:
                          k -= 1
                  else:
                      j += 1
                      while j < k and nums[j] == nums[j - 1]:
                          j += 1
          return res
  ```
  &emsp;&emsp;最终结果，*运行时间144ms*，超过51.14%；*占用内存13.1MB*，超过48.75%。
  > 这里两个注释中间的 if - else 部分可以并入下方的判断分支，实际上起到了一样的效果。但由于实际上两个分支只会进入一个，去掉后会始终进入下方的分支，对最终执行效率没有影响。

* **在边界上进行优化**

  &emsp;&emsp;在最外层循环中，我们可以发现，当第一层指向的数 `nums[i]` 确定时，那么这时无论后面的两个指针指向的数为哪一个，都会存在一个最大值和最小值。**最小值** 为 `nums[i] + nums[i+1] + nums[i+2]`，**最大值** 为 `nums[i] + nums[len(nums)-1] + nums[len(nums)-2]`。那么我就可以将这两个值与 `target` 进行比较。

  + 如果最小值都大于 `target` ，那么我们就可以将这个最小值更新为记录值，并且使用 `break` 跳出循环，这里为什么可以直接**跳出循环**呢？因为现阶段的的 `nums[i]` 所能达到的最小值都已经大于 `target` 了，那么当 `i` 继续增加的时候由于数组已经是升序的了，那么这个最小值一定会越来越大，那么它与 `target` 的差也会越来越大。

  + 如果最大值都小于 `target` ，那么我们就可以将这个最大值更新为记录值，并且使用 `continue` 跳过当前轮循环，这里为什么不使用 `break` 了呢。因为当 `i` 增加时，这个最大值也会跟着增加，会使其与 `target` 可能减小。

  ```python
      min_sum = nums[i] + nums[j] + nums[j+1]
      max_sum = nums[i] + nums[k-1] + nums[k]
      if min_sum > target:
          if abs(min_sum - target) < abs(res - target):
              res = min_sum
              break
      if max_sum < target:
          if abs(max_sum - target) < abs(res - target):
              res = max_sum
              continue
  ```
  &emsp;&emsp;最终结果，*运行时间88ms*，超过95.13%；*占用内存13MB*，超过47.01%。
  > 添加在 for 循环中， while 之前
