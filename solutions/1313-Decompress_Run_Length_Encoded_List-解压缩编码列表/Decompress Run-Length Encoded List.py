# python3
# simple
# 数组
# 36ms 94.63%
# 13.7MB 100.0%

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        x = nums[::2]
        y = nums[1::2]
        res = []
        for i in range(len(x)):
            res.extend([y[i] for _ in range(x[i])])
        return res
