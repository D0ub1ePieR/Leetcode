# python3
# hard
# 数组
# 36ms 85.58%
# 13.7MB 16.67%

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        import collections
        t = collections.Counter(nums)
        i = 1
        while 1:
            if t[i] == 0:
                return i
            i += 1
