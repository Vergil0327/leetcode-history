class SegmentTree():
    def __init__(self, A, op=min):
        n = len(A)

        self.st = st = ([0]*n+A)
        for i in range(n-1, 0, -1):
            st[i] = op(st[i<<1], st[i<<1|1])

        self.op = op
        self.n = n

    def __getitem__(self, i):
        return self.st[i+self.n]

    def __setitem__(self, i, v):
        st, op, n = self.st, self.op, self.n
        i += n
        st[i] = v

        while i:
            st[i>>1] = op(st[i], st[i^1])
            i >>= 1

    # 雙閉區間 [l,r] both inclusive
    def query(self, l, r):
        st, op , n = self.st, self.op, self.n
        l, r = l+n, r+n

        res = float('inf') if op == min else -float('inf')
        while l <= r:
            if l == r:
                res = op(res, st[l])
                break
            if l&1 == 1:
                res = op(res, st[l])
                l += 1
            if r&1 == 0:
                res = op(res, st[r])
                r -= 1
            l, r = l >> 1, r >> 1

        return res
    
import heapq
class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        rootMax = SegmentTree(nums, max)
        rootMin = SegmentTree(nums, min)
        value = lambda l, r : rootMax.query(l, r) - rootMin.query(l, r)

        pq = []
        for l in range(n):
            heapq.heappush(pq, [-value(l, n-1), l, n-1])

        res = 0
        while k:
            negVal, l, r = heapq.heappop(pq)
            res += -negVal

            if l <= r-1:
                heapq.heappush(pq, [-value(l, r-1), l, r-1])
            k -= 1
        return res