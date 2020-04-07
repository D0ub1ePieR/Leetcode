# 33、搜索旋转排序数组
> tag: python 、 数组 、 二分查找

***
### 题目描述

&emsp;&emsp;假设按照升序排序的数组在预先未知的某个点上进行了旋转。

&emsp;&emsp;( 例如，数组 `[0,1,2,4,5,6,7]` 可能变为 `[4,5,6,7,0,1,2]` )。

&emsp;&emsp;搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 `-1` 。

&emsp;&emsp;你可以假设数组中不存在重复的元素。

&emsp;&emsp;你的算法时间复杂度必须是 `O(log n)` 级别。

### 示例1

```
  输入: nums = [4,5,6,7,0,1,2], target = 0
  输出: 4
```

### 示例2

```
  输入: nums = [4,5,6,7,0,1,2], target = 3
  输出: -1
```

***
### 题目链接
[33.搜索旋转排序数组](https://leetcode-cn.com/problems/search-in-rotated-sorted-array/)

***
### 题解

* **函数**

&emsp;&emsp;直接使用数组的 `index` 函数进行查找 `target` 所处的位置，但是由于如果数组中不存在 `target` 会报错，便使用 `try-except-else` 结构。

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        try:
            res = nums.index(target)
        except:
            return -1
        else:
            return res
```

&emsp;&emsp;最终结果，*运行时间48ms*，超过40.88%；*占用内存13.8MB*，超过5.24%。

* **线性查找**

&emsp;&emsp;忽略题设中的时间复杂度要求，使用线性查找，首先由最左开始查找，直到当前元素比 `target` 大或是下一个元素小于当前元素时停止第一阶段寻找。记录数组当前位置，即旋转的位置。随后开始第二轮寻找，从数组最右开始，直到当前元素比 `target` 小或到达了旋转位置即停止。

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums == []:
            return -1
        index = 0
        while index < len(nums)-1 and nums[index] < target and nums[index] < nums[index+1]:
            index += 1
        if nums[index] == target:
            return index
        mid = index
        index = len(nums) - 1
        while nums[index] > target and index > mid:
            index -= 1
        if nums[index] == target:
            return index
        return -1
```

&emsp;&emsp;最终结果，*运行时间44ms*，超过59.22%；*占用内存13.8MB*，超过5.24%。

* **二分查找**

&emsp;&emsp;使用基于顺序数组的二分查找，只是在更新 `left` 以及 `right` 指针时需要分情况讨论。

- 当 `nums[mid] >= nums[left]` 时，说明当前段中左侧是按照顺序排列的，那么

  + 如果 `target` 在左侧，即 `nums[left] <= target < nums[min]`，则将搜索区域转变为左侧， `right = mid - 1`

  + 否则在不按顺序排列的右侧继续寻找 `target`，则 `left = mid + 1`

- 否则则说明当前段中右侧是按照顺序排列的，那么

  + 如果 `target` 在右侧，即 `nums[mid] < target <= nums[right]`，则将搜索区域转变为右侧， `left = mid + 1`

  + 否则在不按顺序排列的左侧继续寻找 `target`，则 `right = mid - 1`

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        if nums == []:
            return -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[left]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
```

&emsp;&emsp;最终结果，*运行时间64ms*，超过11.94%；*占用内存13.8MB*，超过5.24%。可以发现尽管时间复杂度更优，但是实际巡行时竟然是耗时最长的。
