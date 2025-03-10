# Ref. Template
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

        res = (float("inf"), -1)
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

class SegmentTree:
    def __init__(self, leaf_nodes, op=max):
        size = len(leaf_nodes)
        self.op = op
        self.n = 2 ** math.ceil(math.log2(size))
        self.st = [0] * (2 * self.n)
        for i, val in enumerate(leaf_nodes):
            self.__setitem__(i, val)

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

        res = 0
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

    """
    find leftmost element which is gte target_val
    return original index if valid element exists else -1
    """
    def find(self, target_val):
        if self.st[1] < target_val:
            return -1

        i = 1
        while i < self.n:
            if self.st[i * 2] >= target_val:
                i = i * 2
            else:
                i = i * 2 + 1
        return i-self.n