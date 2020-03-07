# python3
# simple
# 哈希表 数学
# 48ms 31.73%
# 13.4MB 15.50%

class Solution:
    def isHappy(self, n: int) -> bool:
        record = []
        while 1:
            s = sum([int(x)**2 for x in str(n)])
            if s == 1:
                return True
            if s in record:
                return False
            record.append(s)
            n = s

# 56ms 18.34%
# 13.4MB 15.50%

class Solution:
    def isHappy(self, n: int) -> bool:
        def cal_sum(num):
            s = sum([int(x)**2 for x in str(num)])
            # s = 0
            # while num != 0:
            #    s += (num % 10) ** 2
            #    num //= 10
            # return s
        slow = fast = n
        while 1:
            slow = cal_sum(slow)
            fast = cal_sum(cal_sum(fast))
            if slow == fast:
                break
        return slow == 1
