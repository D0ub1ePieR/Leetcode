# python3
# simple
# 数组 双指针
# 248ms 82.29%
# 15.7MB 5.36%

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted([x**2 for x in A])
