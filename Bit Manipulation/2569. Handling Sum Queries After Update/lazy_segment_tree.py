from typing import List
from collections import defaultdict

class Solution:
    def handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums1)
        seg = LazySegmentTreeSum(nums1)
        sum2 = sum(nums2)
        res = []
        for _type, a, b in queries:
            if _type == 1:
                seg.updateRange(a, b)
            elif _type == 2:
                sum2 += seg.queryRange(0, n) * a
            else:
                res.append(sum2)
        return res

class LazySegmentTreeSum:
    def __init__(self, nums: List[int]):
        self.n = n = len(nums)
        self.tree = tree = defaultdict(lambda: [0, 0])
        self.lazyTag = defaultdict(int)
        self.lazy = defaultdict(int)

        def init_tree(i, l, r):
            if r < l or l >= len(nums): return
            if l == r:
                tree[i] = [nums[l], 1] # [value, length], we need to know the length for flip values
                return

            mid = l + (r-l)//2
            if l != r: # if l=r, it'll cause dead loop
                init_tree(2*i, l, mid)
            init_tree(2*i+1, mid+1, r)

            tree[i][0] = tree[2*i][0] + tree[2*i+1][0]
            tree[i][1] = tree[2*i][1] + tree[2*i+1][1]
        init_tree(1, 0, n)

    def pushDown(self, i: int):
        lazyTag = self.lazyTag
        lazy = self.lazy
        tree = self.tree
        if lazyTag[i]:
            if lazy[i]%2 == 1:
                lazyTag[2*i] ^= 1
                lazy[2*i] += lazy[i]
                tree[2*i][0] = tree[2*i][1] - tree[2*i][0]
                
                lazyTag[2*i+1] ^= 1
                lazy[2*i+1] += lazy[i]
                tree[2*i+1][0] = tree[2*i+1][1] - tree[2*i+1][0]

                lazyTag[i] = lazy[i] = 0

    def updateRange(self, l: int, r: int) -> None:
        root, n = 1, self.n
        return self._updateRange(root, 0, n, l, r)
    def _updateRange(self, i: int, start: int, end: int, l: int, r: int, val: int = 0) -> None:
        if r < start or l > end: return # outside [l, r], not covered by [l, r]
        if l <= start and end <= r: # completely covered within [l, r]
            ### own update logic here
            # because nums[i] = 0 or 1
            # after flips, [start, end] -> sum = total_length - sum
            self.tree[i][0] = self.tree[i][1] - self.tree[i][0]
            self.lazyTag[i] ^= 1
            self.lazy[i] += 1 # flip once
            return
        
        mid = start + (end-start)//2
        self.pushDown(i)
        self._updateRange(2*i, start, mid, l, r, val)
        self._updateRange(2*i+1, mid+1, end, l, r, val)
        self.tree[i][0] = self.tree[2*i][0] + self.tree[2*i+1][0]

    def queryRange(self, l: int, r: int) -> int:
        root, n = 1, self.n
        return self._queryRange(root, 0, n, l, r)
    def _queryRange(self, i: int, ll: int, rr: int, l: int, r: int) -> int:
        # outside
        if r < ll or l > rr: return

        # inside
        if l >= ll and r <= rr: return self.tree[i][0]

        mid = l + (r-l)//2
        self.pushDown(i)
        return self._queryRange(2*i, ll, rr, l, mid) + self._queryRange(2*i+1, ll, rr, mid+1, r)



# Lazy Segment Tree: https://leetcode.com/problems/handling-sum-queries-after-update/solutions/3201913/python-segmentation-tree-with-lazy-propogation-explanation/?orderBy=most_votes
class Solution:
    def handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums1)
        seg = LazySegTree(len(nums1), nums1)
        res = []
        ans = sum(nums2)
        
        for _type, a, b in queries:
            if _type == 1:
                seg.update(1, a, b, 0, n)
            if _type == 2:
                ans += seg.query(1, 0, n, 0, n) * a
            if _type == 3:
                res.append(ans)
        return res
    
class LazySegTree():
    def __init__(self, n, nums):
        self.lazy = defaultdict(int)
        self.len = defaultdict(int)
        self.tree = defaultdict(int)
        # initial length and summation
        self.init_len(1, 0, n, 0, n, nums)
        self.init_num(1, 0, n, 0, n, nums)
        
    def init_len(self, i, ul, ur, l, r, num):
        if r < l or l >= len(num):
            return 0
        if r == l:
            self.len[i] = 1
            return 1
        mid = l + (r-l)//2
        if l != r:
            self.init_len(i*2, ul, ur, l, mid, num)
        self.init_len(i*2+1, ul, ur, mid+1, r, num)
        self.len[i] = self.len[i*2] + self.len[i*2+1]
    
    def init_num(self, i, ul, ur, l, r, num):
        if r < l or l >= len(num):
            return
        if l == r:
            self.tree[i] = num[l]
            return
        mid = l + (r-l)//2
        if l != r:
            self.init_num(i*2, ul, ur, l, mid, num)
        self.init_num(i*2+1, ul, ur, mid+1, r, num)
        
        self.tree[i] = self.tree[i*2] + self.tree[i*2+1]
        
    
    def proplazy(self, i):
        # if the parent node has the notation to flip, then we update all summation of children nodes.
        if self.lazy[i]:
            self.lazy[i*2] ^= self.lazy[i]
            self.tree[i*2] = self.len[i*2] - self.tree[i*2]
            self.lazy[i*2 + 1] ^= self.lazy[i]
            self.tree[i*2 + 1] = self.len[i*2+1] - self.tree[i*2 + 1]
            self.tree[i] = self.tree[i*2] + self.tree[i*2+1]
            self.lazy[i] = 0
        
    def update(self, i, ul, ur, l, r):
        if l > ur or r < ul:
            return 
        if ul <= l and r <= ur:
            # mark to flip
            self.lazy[i] ^= 1
            self.tree[i] = self.len[i] - self.tree[i]
        else:
            mid = (l + r) // 2
            self.proplazy(i)
            self.update(i*2, ul, ur, l, mid)
            self.update(i*2+1, ul, ur, mid+1, r)
            self.tree[i] = self.tree[i*2] + self.tree[i*2+1]
           
    def query(self, i, ul, ur, l, r):
        if l > ur or r < ul:
            return 0
        if ul <= l and r <= ur:
            return self.tree[i]
        else:
            mid = (l + r) // 2
            self.proplazy(i)
            return self.query(i*2, ul, ur, l, mid) + self.query(i*2+1, ul, ur, mid+1, r)
        