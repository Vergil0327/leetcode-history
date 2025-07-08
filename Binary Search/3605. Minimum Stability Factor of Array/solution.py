from math import gcd, log2

def build_sparse_table(nums):
    n = len(nums)
    max_log = int(log2(n)) + 1
    st = [[0]*max_log for _ in range(n)]

    for i in range(n):
        st[i][0] = nums[i]

    for j in range(1, max_log):
        for i in range(n - (1 << j) + 1):
            st[i][j] = gcd(st[i][j-1], st[i + (1 << (j-1))][j-1])
    
    return st

def query_gcd(st, l, r):  # [l, r)
    length = r - l
    k = int(log2(length))
    return gcd(st[l][k], st[r - (1 << k)][k])

class Solution:
    def minStable(self, nums: List[int], maxC: int) -> int:
        n = len(nums)

        range_gcd = build_sparse_table(nums)

        l, r = 0, n + 1
        while l + 1 < r:
            mid = (l + r) // 2
            if self.count(nums, mid, range_gcd) <= maxC:
                r = mid
            else:
                l = mid
        return l

    def count(self, nums: List[int], length: int, table: List[List[int]]) -> int:
        n = len(nums)

        cnt = 0
        l = 0
        while l + length - 1 < n:
            g = query_gcd(table, l, l+length)

            if g > 1:
                cnt += 1
                l += length
            else:
                l += 1
        return cnt