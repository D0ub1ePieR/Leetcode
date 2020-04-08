# 153、寻找旋转排序数组中的最小值
>tag: python3 、 数组 、 二分查找

***
### 题目描述

&emsp;&emsp;假设按照升序排序的数组在预先未知的某个点上进行了旋转。

&emsp;&emsp;( 例如，数组 `[0,1,2,4,5,6,7]` 可能变为 `[4,5,6,7,0,1,2]` )。

&emsp;&emsp;请找出其中最小的元素。

&emsp;&emsp;你可以假设数组中不存在重复元素。

### 示例1

```
  输入: [3,4,5,1,2]
  输出: 1
```

### 示例2

```
  输入: [4,5,6,7,0,1,2]
  输出: 0
```

***
### 题目链接
[153.寻找旋转排序数组中的](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/)

***
### 题解

使用 [搜索旋转排序数组](33-Search_in_Rotated_Sorted_Array-搜索旋转排序数组) 中的二分搜索方法。

* **min** 函数

&emsp;&emsp;可以直接使用库函数 `min` 寻找数组最小的数，但是效率并不是很高。

* **二分查找**

&emsp;&emsp;对 `nums[mid]` 进行讨论：

- 如果 `nums[mid] >= nums[left]` ，说明左侧是按照递增的顺序排列的，那么判断 `nums[left]` 是否比当前最小值小，随后进入右侧搜索， `left = mid + 1`

- 否则说明右侧是按照递增的顺序排列的，判断 `nums[right]` 是否比当前最小值小，随后进入左侧继续搜索， `right = mid - 1`

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        res = nums[0]
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < res:
                res = nums[mid]
            if nums[mid] >= nums[left]:
                if nums[left] < res:
                    res = nums[left]
                left = mid + 1
            else:
                if nums[right] < res:
                    res = nums[right]
                right = mid - 1
        return res
```

&emsp;&emsp;最终结果，*运行时间36ms*，超过87.08%；*占用内存13.5MB*，超过5.04%。
