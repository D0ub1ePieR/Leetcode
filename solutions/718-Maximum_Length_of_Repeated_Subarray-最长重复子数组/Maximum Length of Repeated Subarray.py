# python3
# medium
# 数组 二分查找 哈希表 动态规划
# 2996ms 88.42%
# 39.1MB 6.00%

class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        dp = [[0] * (len(B) + 1) for i in range(len(A) + 1)]
        for i in range(len(A)-1, -1, -1):
            for j in range(len(B)-1, -1, -1):
                if A[i] == B[j]:
                    dp[i][j] = dp[i+1][j+1] + 1
        return max(max(row) for row in dp)
