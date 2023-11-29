class SegmentTree:
    def __init__(self, arr, op):
        self.n = n = max(arr)
        self.st = st = [0]*n + [0]*n
        self.op = op

    # [l,r] both inclusive
    def query(self, l, r):
        st, op, n = self.st, self.op, self.n

        res = 0
        l, r = l+n, r+n
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
            l, r = l>>1, r>>1
        return res
    
    def update(self, i, v):
        st, op, n = self.st, self.op, self.n
        i += n
        st[i] = v

        while i:
            st[i>>1] = op(st[i], st[i^1])
            i >>= 1

class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        st = SegmentTree(nums, max)

        res = 1
        for num in nums:
            num -= 1 # to 0-indexed
            length = st.query(max(0, num-k), num-1)
            res = max(res, length+1)
            st.update(num, length+1)
        return res