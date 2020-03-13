# python3
# hard
# 堆 数学 动态规划
# 108ms 96.62%
# 13.7MB 5.02%

class Ugly:
    def __init__(self):
        self.nums = [1]
        for i in range(1691):
            if self.nums[i] * 2 not in self.nums:
                bisect.insort(self.nums, self.nums[i]*2)
            if self.nums[i] * 3 not in self.nums:
                bisect.insort(self.nums, self.nums[i]*3)
            if self.nums[i] * 5 not in self.nums:
                bisect.insort(self.nums, self.nums[i]*5)

class Solution:
    u = Ugly()
    def nthUglyNumber(self, n: int) -> int:
        return self.u.nums[n-1]
            

# 3052ms 5.03%
# 13.6MB 5.35%

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        l = [1]
        c = 0
        while c < n-1:
            if l[c] * 2 not in l:
                bisect.insort(l, l[c]*2)
            if l[c] * 3 not in l:
                bisect.insort(l, l[c]*3)
            if l[c] * 5 not in l:
                bisect.insort(l, l[c]*5)
            c += 1
        return l[c]
