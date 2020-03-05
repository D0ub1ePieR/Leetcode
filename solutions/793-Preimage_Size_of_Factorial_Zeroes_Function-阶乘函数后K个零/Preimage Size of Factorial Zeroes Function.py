# python3
# hard
# 二分查找
# 36ms 64.91%
# 13.2MB 52.00%

class Solution:
    def preimageSizeFZF(self, K: int) -> int:
        start, end = K, K * 5 + 1
        if K == 0:
            return 5
        while start < end:
            mid = (start + end) // 2
            tmp = 5
            s = 0
            while mid >= tmp:
                s += mid // tmp
                tmp *= 5
            if s == K:
                return 5
            elif s < K:
                start = mid + 1
            else:
                end = mid - 1
        return 0

# 40ms 49.12%
# 13.4MB 52.00%

class Solution:
    def preimageSizeFZF(self, K: int) -> int:
        ci = 0
        while ci < K:
            ci = ci * 5 + 1
        while K > 0:
            ci = (ci - 1) / 5
            if K / ci >= 5:
                return 0
            K %= ci
        return 5
