# python3
# medium
# 堆 数学
# 328ms 91.21%
# 25.1MB 41.05%

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        import heapq
        l = [1]
        loc = [0] * len(primes)
        heap = []
        visited = set()
        for index, num in enumerate(primes):
            heapq.heappush(heap, [num, index])
            visited.add(num)
        for i in range(1, n):
            t, k = heapq.heappop(heap)
            l.append(t)
            while primes[k] * l[loc[k]] in visited:
                loc[k] += 1
            heapq.heappush(heap, [primes[k]*l[loc[k]], k])
            visited.add(primes[k]*l[loc[k]])
        return l[-1]

# 1028ms 52.75%
# 17.3MB 44.21%

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        l = [1]
        loc = [0] * len(primes)
        for i in range(1, n):
            l.append(min(x * l[y] for x, y in zip(primes, loc)))
            for j in range(len(primes)):
                if l[i] >= primes[j] * l[loc[j]]:
                    loc[j] += 1
        return l[-1]

# 1764ms 5.22%
# 116.9MB 5.26%

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        import heapq
        l = [1]
        c = 0
        while c < n - 1:
            t = heapq.heappop(l)
            while l and t == l[0]:
                t = heapq.heappop(l)
            for num in primes:
                heapq.heappush(l, t*num)
            c += 1
        return heapq.heappop(l)
