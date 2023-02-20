class LazySegmentTreeSum:
    def __init__(self, nums: List[int]):
        self.n = n = len(nums)
        self.tree = tree = defaultdict(lambda: [0, 0])
        self.lazyTag = defaultdict(int)
        self.lazy = defaultdict(int)

        def init_tree(i, l, r):
            if r < l or l >= len(nums): return
            if l == r:
                # implement your own business value and store in tree node
                tree[i] = [nums[l], 1] # [value, length], we need to know the length for flip values
                return

            mid = l + (r-l)//2
            if l != r: # if l=r, it'll cause dead loop
                init_tree(2*i, l, mid)
            init_tree(2*i+1, mid+1, r)

            tree[i][0] = tree[2*i][0] + tree[2*i+1][0]
            tree[i][1] = tree[2*i][1] + tree[2*i+1][1]
        init_tree(1, 0, n)

    # propagation lazy tag and value from parent to child nodes
    def pushDown(self, i: int):
        lazyTag = self.lazyTag
        lazy = self.lazy
        tree = self.tree
        if lazyTag[i]:
            if lazy[i]%2 == 1:
                # implement your own business value for lazy tag and lazy value update
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
            ### own business logic here
            self.tree[i][0] = self.tree[i][1] - self.tree[i][0]
            self.lazyTag[i] ^= 1
            self.lazy[i] += 1 # flip once
            return
        
        mid = start + (end-start)//2
        self.pushDown(i)
        self._updateRange(2*i, start, mid, l, r, val)
        self._updateRange(2*i+1, mid+1, end, l, r, val)

        ### implement your own update logic here
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

