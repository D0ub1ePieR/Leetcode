# python3
# simple
# 位运算 数组 数学
# 40ms 96.75%
# 14.8MB 6.06%

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y:x^y, [i for i in range(len(nums)+1)]+nums)

# 44ms 93.03%
# 14.7MB 12.12%

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return len(nums)*(len(nums)+1)//2 - sum(nums)
