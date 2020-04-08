# python3
# medium
# 数组 二分查找
# 36ms 87.08%
# 13.5MB 5.04%

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
