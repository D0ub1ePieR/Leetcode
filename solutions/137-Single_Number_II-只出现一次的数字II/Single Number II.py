# python3
# medium
# 位运算
# 40ms 89.24%
# 15.3MB 25.00%

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return (3*sum(set(nums)) - sum(nums)) // 2

# 44ms 79.18%
# 14.8MB 25.00%

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        once, twice = 0, 0
        for i in nums:
            once = (once ^ i) & (~twice)
            twice = (twice ^ i) & (~once)
        return once
