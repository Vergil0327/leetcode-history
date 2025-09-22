# Intuition

`value(l, r) = max(nums[l:r]) - min(nums[l:r])`
我們目標要找出前k大的value(l, r), 其中(l, r)必須是distinct subarray的左右端點

從關係式可看出我們需要高校查找**range max**以及**range min**的方法 => 想到segment tree

所以首先建立segment tree for max & min

```py
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

rootMax = SegmentTree(nums, max)
rootMin = SegmentTree(nums, min)
value = lambda l, r : rootMax.query(l, r) - rootMin.query(l, r)
```

如此一來, 再來就是想辦法找出前k大的subarray value了
帶點**greedy**的方式想, subarray涵蓋越多元素, 越可能包含max及min而產生較大value
所以我們把遍歷所有左端點跟最右端點`n-1`配對: `[l, n-1] for l in range(n)`
將這些subarray加入到max heap `pq`裡: `[-value(l, n-1), l, n-1 for l in range(n)]`

然後開始嘗試挑出value前k大的subarray
每找出當前最大value的subarray, 就將右端點往左一格產生新的subarray放入max heap裡
直到找出k個