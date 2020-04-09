# python3
# medium
# 数组
# 60ms 72.83%
# 14.5MB 50.00%

class Solution:
    def constructArray(self, n: int, k: int):
        if n == 1:
            return None
        elif k == 1:
            return list(range(1, n+1))
        else:
            res = list(range(1, n-k))
            i, j = max(n-k, 1), n
            while i<=j:
                if i == j:
                    res.append(i)
                else:
                    res.append(i)
                    res.append(j)
                i += 1
                j -= 1
        return res

# 372ms 37.50%
# 14.7MB 33.33%

class Solution:
    def constructArray(self, n: int, k: int):
        res = list(range(1, n+1))
        for i in range(1, k):
            res[i:] = res[:i-1:-1]
        return res

# - -
# - -

class Solution:
    def constructArray(self, n: int, k: int):
        def construct(l, l_res, minus, k):
            if l_res == []:
                if len(minus) == k:
                    return l, True
                else:
                    return None, False
            for i in l_res:
                if l == []:
                    tmp = l_res[:]
                    tmp.remove(i)
                    res, flag = construct([i], tmp, [], k)
                    if flag:
                        return res, True
                elif len(minus) == k:
                    if abs(i - l[-1]) in minus:
                        tmp, tmp_res = l[:], l_res[:]
                        tmp.append(i)
                        tmp_res.remove(i)
                        res, flag = construct(tmp, tmp_res, minus, k)
                        if flag:
                            return res, True
                else:
                    tmp, tmp_res, tmp_minus = l[:], l_res[:], minus[:]
                    if abs(i - l[-1]) in minus:
                        tmp.append(i)
                        tmp_res.remove(i)
                        res, flag = construct(tmp, tmp_res, minus, k)
                        if flag:
                            return res, True
                    else:
                        tmp.append(i)
                        tmp_res.remove(i)
                        tmp_minus.append(abs(i - l[-1]))
                        res, flag = construct(tmp, tmp_res, tmp_minus, k)
                        if flag:
                            return res, True
            return None, False
        res, flag = construct([], list(range(1, n+1)), [], k)
        return res
