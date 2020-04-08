# python3
# medium
# 数组 二分查找
# 36ms 92.63%
# 14MB 8.00%

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        nums = list(set(nums))
        left, right = 0, len(nums) - 1
        if nums == []:
            return False
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True

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
        return False

# 40ms 82.96%
# 13.7MB 8.20%

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if nums == []:
            return False
        index = 0
        while index < len(nums)-1 and nums[index] < target and nums[index] <= nums[index+1]:
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

# 44ms 72.41%
# 13.9MB 8.20%

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        return target in nums
