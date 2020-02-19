# python3
# medium
# 哈希表 二分查找
# 284ms 83.26%
# 50MB 19.72%

class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        a = collections.Counter(A)
        b = collections.Counter(B)
        c = collections.Counter(C)
        d = collections.Counter(D)
        dict1 = {}
        for i in a:
            for j in b:
                dict1[i+j] = dict1.get(i+j, 0) + a[i]*b[j]
        res = 0
        for i in c:
            for j in d:
                if -i-j in dict1:
                    res += c[i] * d[j] * dict1[-i-j]
        return res

# 432ms 24.34%
# 75.3MB 5.28%

class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        a = collections.Counter(A)
        b = collections.Counter(B)
        c = collections.Counter(C)
        d = collections.Counter(D)
        dict1 = {}
        dict2 = {}
        for i in a:
            for j in b:
                dict1[i+j] = dict1.get(i+j, 0) + a[i]*b[j]
        for i in c:
            for j in d:
                dict2[i+j] = dict2.get(i+j, 0) + c[i]*d[j]
        res = 0
        for num in dict1:
            res += dict1[num] * dict2.get(-num, 0)
        return res

# 704ms 5.12%
# 65.6MB 5.28%

class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        l = len(A)
        dict1 = {}
        dict2 = {}
        for i in range(l):
            for j in range(l):
                sum1 = A[i] + B[j]
                sum2 = C[i] + D[j]
                dict1[sum1] = dict1.get(sum1, 0) + 1
                dict2[sum2] = dict2.get(sum2, 0) + 1
        res = 0
        for num in dict1:
            res += dict1[num] * dict2.get(-num, 0)
        return res
