# 81、搜索旋转排序数组II
> tag: python 、 数组 、 二分查找

***
### 题目描述

&emsp;&emsp;假设按照升序排序的数组在预先未知的某个点上进行了旋转。

&emsp;&emsp;( 例如，数组 `[0,0,1,2,2,5,6]` 可能变为 `[2,5,6,0,0,1,2]` )。

&emsp;&emsp;编写一个函数来判断给定的目标值是否存在于数组中。若存在返回 `true`，否则返回 `false`。

### 示例1

```
  输入: nums = [2,5,6,0,0,1,2], target = 0
  输出: true
```

### 示例2

```
  输入: nums = [2,5,6,0,0,1,2], target = 3
  输出: false
```

**进阶**：

* 这是 搜索旋转排序数组 的延伸题目，本题中的 nums  可能包含重复元素。

* 这会影响到程序的时间复杂度吗？会有怎样的影响，为什么？

***
### 题目连接
[81.搜索旋转排序数组II](https://leetcode-cn.com/problems/search-in-rotated-sorted-array-ii/)

***
### 题解

与 [搜索旋转排序数组](../33-Search_in_Rotated_Sorted_Array-搜索旋转排序数组) 类似，直接将三种方法转移至这道题中。由于这道题只要返回 `True` 或 `False`，以及可能会出现相同的数字，还需要对方法进行一定的修改。

* **函数**

&emsp;&emsp;因为只要返回 `target` 是否在数组中即可，因此不需要考虑数组的顺序直接返回即可。

```python
  return target in nums
```

&emsp;&emsp;最终结果，*运行时间44ms*，超过72.41%；*占用内存13.9MB*，超过8.20%。

* **线性查找**

&emsp;&emsp;在原来的基础上由于可能会出现相同的数字，则要在判断排序旋转点的位置时，不需要为严格递增，只要大于等于即可

```python
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if nums == []:
            return False
        index = 0
        while index < len(nums)-1 and nums[index] < target and nums[index] <= nums[index+1]:  # < --> <=
            index += 1
        if nums[index] == target:
            return True
        mid = index
        index = len(nums) - 1
        while nums[index] > target and index > mid:
            index -= 1
        if nums[index] == target:
            return True
        return False
```

&emsp;&emsp;最终结果，*运行时间40ms*，超过82.96%；*占用内存13.7MB*，超过8.20%。

* **二分查找**

&emsp;&emsp;由于可能会出现相同的数字，所以在判断 `mid` 左右两侧是否已经按顺序排布的时候会产生错误，例如

```
  [1, 2, 1, 1, 1]
   |     |     |
   left  mid   right
```

于是，用一个简单的方法，直接将 `nums` 数组转变为 `set` 集合，在转换为 `list` 数组，执行原来的步骤便可以很快的将方法转换问题。

```python
  nums = list(set(nums))
```

&emsp;&emsp;最终结果，*运行时间36ms*，超过92.63%；*占用内存14MB*，超过8.00%。可以发现当可能有重复数字出现时，二分查找的时间复杂度优势便体现了出来。主要原因可能是

- 当不存在重复元素的时候，数组最大值为 `k`，那么数组最多只有 `k` 个元素，这时查找 `k` 次和 `log(k)` 次的差距可能不会很大，尤其当 `k` 较小的时候，实际上测试用例中的数组元素有很多也不是很大

- 当存在重复元素的时候，不论是用 `python` 的数组查找还是线性的查找，对于重复元素都要进行重复的操作，而二分查找虽然不会对重复元素进行区分，但是大量的重复元素会导致数组元素上界会很大， `log(k)` 的优势便会体现出来
