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
        
class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        seg = SegmentTree(baskets)
        res = 0
        for val in fruits:
            node_idx = seg.find(val)

            if node_idx != -1:
                seg[node_idx] = -1
            else:
                res += 1
        return res