from collections import defaultdict
from math import isqrt

class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        mod = 10**9 + 7
        n = len(nums)
        boundary = isqrt(n) + 1
        events = defaultdict(lambda: [1] * n)

        for l, r, k, v in queries:
            if k <= boundary:
                events[k][l] = events[k][l] * v % mod
                r2 = r + ((l - r) % k or k)
                if r2 < n:
                    events[k][r2] = events[k][r2] * pow(v, mod - 2, mod) % mod
            else:
                for i in range(l, r + 1, k):
                    nums[i] = nums[i] * v % mod

        for k, row in events.items():
            for start in range(k):

                # 類似計算diff array總和, 只是改乘法
                mul = 1
                for j in range(start, n, k):
                    mul = mul * row[j] % mod
                    nums[j] = nums[j] * mul % mod

        ans = 0
        for x in nums:
            ans ^= x
        return ans