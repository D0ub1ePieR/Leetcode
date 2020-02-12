# python3
# simple
# 双指针 数组 二分查找
# 72ms 73.28%
# 13.5MB 48.12%

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start, end = 0, len(numbers) - 1
        while numbers[start] + numbers[end] != target:
            if numbers[start] + numbers[end] > target:
                end -= 1
            else:
                start += 1
        return [start + 1, end + 1]
