# python3
# medium
# 数组 二分查找
# 44ms 58.22%
# 13.8MB 5.24%

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

# 48ms 40.88%
# 13.8MB 5.24%

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        try:
            res = nums.index(target)
        except:
            return -1
        else:
            return res

# 64ms 11.94%
# 13.8MB 5.24%

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
