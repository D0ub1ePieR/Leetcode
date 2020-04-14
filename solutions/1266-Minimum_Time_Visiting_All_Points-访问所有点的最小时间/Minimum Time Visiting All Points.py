# python3
# simple
# 几何 数组
# 72ms 57.09%
# 13.6MB 11.11%

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        return sum([max(abs(points[i][0]-points[i-1][0]), abs(points[i][1]-points[i-1][1])) for i in range(1,len(points))])
