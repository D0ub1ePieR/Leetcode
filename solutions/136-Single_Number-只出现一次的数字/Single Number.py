# python3
# simple
# 位运算 哈希表
# 48ms 75.94%
# 15.4MB 5.26%

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x^y, nums)
