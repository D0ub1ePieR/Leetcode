# python3
# medium
# 数组 数学
# 32ms 75.33%
# 13.4MB 28.13%

class Solution:
    def maximumSwap(self, num: int) -> int:
        numbers = list(str(num))
        sort_num = sorted(numbers[:])
        sort_num.reverse()
        reverse_num = numbers[:]
        reverse_num.reverse()
        for i in range(len(numbers)):
            if numbers[i] != sort_num[i]:
                index = reverse_num.index(sort_num[i])
                t = numbers[-(index+1)]
                numbers[-(index+1)] = numbers[i]
                numbers[i] = t
                break
        return int(''.join(numbers))
