class SegmentTree:
    def __init__(self, arr, op):
        self.n = n = len(arr)
        self.op = op
        self.st = st = [0]*n + arr
        for i in range(n-1, 0, -1):
            st[i] = op([st[i<<1], st[i<<1|1]])
        
    def __getitem__(self, i):
        return self.st[i+self.n]
    def __setitem__(self, i, val):
        st, op, n = self.st, self.op, self.n
        i += n
        st[i] = val

        while i:
            st[i>>1] = op([st[i], st[i^1]])
            i >>= 1

    def query(self, l, r): # query range [l,r]
        st, op, n = self.st, self.op, self.n
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
            l, r = l>>1, r>>1
        return res


class BookMyShow:

    def __init__(self, n: int, m: int):
        self.n, self.m = n, m
        self.rootSum = SegmentTree([m]*n, sum)
        self.rootMax = SegmentTree([m]*n, max)

        self.seats = seats = [0]*n
        self.startRow = 0
        for row in range(n):
            seats[row] = m
        

    def gather(self, k: int, maxRow: int) -> List[int]:
        m, seats = self.m, self.seats
        l, r = 0, maxRow
        while l < r:
            mid = l + (r-l)//2
            if self.rootMax.query(0, mid) >= k:
                r = mid
            else:
                l = mid+1

        if self.rootMax.query(l, l) < k: return []

        res = [l, m-seats[l]]

        seats[l] -= k
        self.rootSum[l] = seats[l]
        self.rootMax[l] = seats[l]

        return res

    def scatter(self, k: int, maxRow: int) -> bool:
        rootSum = self.rootSum
        rootMax = self.rootMax
        seats = self.seats

        if rootSum.query(0, maxRow) < k: return False

        # 逐row分配ticket
        while k > 0:
            tickets = min(k, seats[self.startRow])
            seats[self.startRow] -= tickets
            k -= tickets

            rootSum[self.startRow] = seats[self.startRow]
            rootMax[self.startRow] = seats[self.startRow]
            if seats[self.startRow] == 0:
                self.startRow += 1

        return True
    
# Recursive
    
class Node:
    def __init__(self, l, r) -> None:
        self.l, self.r = l, r
        self.left = self.right = None
        self.info = self.lazy_tag = self.lazy_val = 0 

class LazySegmentTreeSum:
    def __init__(self, l: int, r: int, val: int): # inti range [l,r] with val
        def init_tree(l, r, val):
            node = Node(l, r)
            if l == r:
                node.info = val
                return node
            
            mid = (l+r)//2
            if node.left == None:
                node.left = init_tree(l, mid, val)
                node.right = init_tree(mid+1, r, val)
                node.info = node.left.info + node.right.info
            return node
        self.root = init_tree(l, r, val)

    # propagation lazy tag and value from parent to child nodes
    def pushDown(self, node):
        if node.lazy_tag == 1 and node.left:
            node.left.info = node.lazy_val * (node.left.r - node.left.l + 1)
            node.right.info = node.lazy_val * (node.right.r - node.right.l + 1)

            node.left.lazy_tag = 1
            node.left.lazy_val = node.lazy_val
            
            node.right.lazy_tag = 1
            node.right.lazy_val = node.lazy_val
            node.lazy_tag = node.lazy_val = 0

    def updateRange(self, l: int, r: int, val: int) -> None:
        def update(node, l, r, val):
            if r < node.l or l  > node.r: return # not dovered by [l,r]

            if l <= node.l and node.r <= r:
                node.info = val * (node.r-node.l+1)
                node.lazy_tag = 1
                node.lazy_val = val
                return
            
            if node.left:
                self.pushDown(node)
                update(node.left, l, r, val)
                update(node.right, l, r, val)
                node.info = node.left.info + node.right.info

        return update(self.root, l, r, val)

    def queryRange(self, l: int, r: int) -> int:
        def query(node, l, r):
            if r < node.l or l > node.r: return 0

            if l <= node.l and node.r <= r:
                return node.info
            
            if node.left:
                self.pushDown(node)
                res = query(node.left, l, r) + query(node.right, l, r)
                node.info = node.left.info + node.right.info
                return res
            
            return node.info # should not reach here
        return query(self.root, l, r)

class LazySegmentTreeMax:
    def __init__(self, l: int, r: int, val: int): # inti range [l,r] with val
        def init_tree(l, r, val):
            node = Node(l, r)
            if l == r:
                node.info = val
                return node
            
            mid = (l+r)//2
            if node.left == None:
                node.left = init_tree(l, mid, val)
                node.right = init_tree(mid+1, r, val)
                node.info = node.left.info + node.right.info
            return node
        self.root = init_tree(l, r, val)

    # propagation lazy tag and value from parent to child nodes
    def pushDown(self, node):
        if node.lazy_tag == 1 and node.left:
            node.left.info = node.info
            node.right.info = node.info

            node.left.lazy_tag = 1
            node.right.lazy_tag = 1
            
            node.lazy_tag = 0

    def updateRange(self, l: int, r: int, val: int) -> None:
        def update(node, l, r, val):
            if r < node.l or l  > node.r: return # not dovered by [l,r]

            if l <= node.l and node.r <= r:
                node.info = val
                node.lazy_tag = 1
                return
            
            if node.left:
                self.pushDown(node)
                update(node.left, l, r, val)
                update(node.right, l, r, val)
                node.info = max(node.left.info, node.right.info)

        return update(self.root, l, r, val)

    def queryRange(self, l: int, r: int) -> int:
        def query(node, l, r):
            if r < node.l or l > node.r: return 0

            if l <= node.l and node.r <= r:
                return node.info
            
            if node.left:
                self.pushDown(node)
                res = max(query(node.left, l, r), query(node.right, l, r))
                node.info = max(node.left.info, node.right.info)
                return res
            
            return node.info # should not reach here
        return query(self.root, l, r)

# Recursive
class BookMyShow:

    def __init__(self, n: int, m: int):
        self.n, self.m = n, m
        self.rootSum = LazySegmentTreeSum(0, n-1, m)
        self.rootMax = LazySegmentTreeMax(0, n-1, m)

        self.seats = seats = [0]*n
        self.startRow = 0
        for row in range(n):
            seats[row] = m
        

    def gather(self, k: int, maxRow: int) -> List[int]:
        m, seats = self.m, self.seats
        l, r = 0, maxRow
        while l < r:
            mid = l + (r-l)//2
            if self.rootMax.queryRange(0, mid) >= k:
                r = mid
            else:
                l = mid+1

        if self.rootMax.queryRange(l, l) < k: return []

        res = [l, m-seats[l]]

        seats[l] -= k
        self.rootSum.updateRange(l, l, seats[l])
        self.rootMax.updateRange(l, l, seats[l])

        return res

    def scatter(self, k: int, maxRow: int) -> bool:
        rootSum = self.rootSum
        rootMax = self.rootMax
        seats = self.seats

        if rootSum.queryRange(0, maxRow) < k: return False

        # 逐row分配ticket
        while k > 0:
            tickets = min(k, seats[self.startRow])
            seats[self.startRow] -= tickets
            k -= tickets

            rootSum.updateRange(self.startRow, self.startRow, seats[self.startRow])
            rootMax.updateRange(self.startRow, self.startRow, seats[self.startRow])
            if seats[self.startRow] == 0:
                self.startRow += 1

        return True