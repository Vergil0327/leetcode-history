# Ref. Template
class SegmentTree():
    def __init__(self, A, op=min):
        n = len(A)

        self.st = st = ([0]*n+A)
        for i in range(n-1, 0, -1):
            st[i] = op([st[i<<1], st[i<<1|1]])

        self.op = op
        self.n = n

    def __getitem__(self, i):
        return self.st[i+self.n]

    def __setitem__(self, i, v):
        st, op, n = self.st, self.op, self.n
        i += n
        st[i] = v

        while i:
            st[i>>1] = op([st[i], st[i^1]])
            i >>= 1
    
    # 雙閉區間 [l,r] both inclusive
    def query(self, l, r):
        st, op , n = self.st, self.op, self.n
        l, r = l+n, r+n

        res = 0
        while l <= r:
            if l == r:
                res = op([res, st[l]])
                break
            if l&1 == 1:
                res = op([res, st[l]])
                l += 1
            if r&1 == 0:
                res = op([res, st[r]])
                r -= 1
            l, r = l >> 1, r >> 1

        return res

class Solution:
    def countOfPeaks(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        
        count = [0]
        for i in range(1, n-1):
            count.append(int(nums[i-1] < nums[i] and nums[i] > nums[i+1]))
        count.append(0)
        
        seg = SegmentTree(count, op=sum)
        
        res = []
        for q in queries:
            if q[0] == 1:
                l, r = q[1], q[2]

                res.append(seg.query(l+1, r-1))
            else:
                idx, val = q[1], q[2]
                nums[idx] = val
                if idx-1>=0:
                    # 若是邊界肯定不是peak所以如果idx-2<0, 那代表idx-1在邊界 => False
                    seg[idx-1] = int((nums[idx-2] < nums[idx-1] if idx-2 >=0 else False) and
                                     nums[idx-1] > nums[idx])

                seg[idx] = int((nums[idx-1] < nums[idx] if idx-1>=0 else False) and 
                               (nums[idx] > nums[idx+1] if idx+1<n else False))
                if idx+1<n:
                    seg[idx+1] = int(nums[idx] < nums[idx+1] and 
                                     (nums[idx+1] > nums[idx+2] if idx+2<n else False))

        return res
