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
        root = self.rootSum
        rootMax = self.rootMax
        seats = self.seats

        if root.query(0, maxRow) < k: return False

        # 逐row分配ticket
        while k > 0:
            tickets = min(k, seats[self.startRow])
            seats[self.startRow] -= tickets
            k -= tickets

            root[self.startRow] = seats[self.startRow]
            rootMax[self.startRow] = seats[self.startRow]
            if seats[self.startRow] == 0:
                self.startRow += 1

        return True