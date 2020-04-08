# python3
# medium
# 回溯算法
# 1080ms 70.52%
# 13.7MB 25.00%

class Solution:
    def __init__(self):
        self.res = 0

    def countArrangement(self, N: int) -> int:
        def count(l, res_l):
            lenth = len(l) + 1
            if res_l == []:
                self.res += 1
                return
            for i in res_l:
                if i % lenth == 0 or lenth % i == 0:
                    tmp, tmp_res = l[:], res_l[:]
                    tmp.append(i)
                    tmp_res.remove(i)
                    count(tmp, tmp_res)
        count([], list(range(1, N+1)))
        return self.res
