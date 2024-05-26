from sortedcontainers import SortedList

class SegmentTree():
    def __init__(self, n, op=max):
        self.st = st = ([0]*(n*2))
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

class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:            
        max_value = max([x[1] for x in queries])
        seg = SegmentTree(max_value+1)
        
        sorted_list = SortedList([0])
        seg[0] = inf
        
        def insert_val(x):
            sorted_list.add(x)
            index = sorted_list.bisect_left(x)
            if index-1 >= 0:
                prev = sorted_list[index-1]
                seg[prev] = x-prev

            if index+1 < len(sorted_list):
                nxt = sorted_list[index+1]
                seg[x] = nxt-x
            else:
                seg[x] = inf # inf-x
        
        ans = []
        for query in queries:
            if query[0] == 1:
                insert_val(query[1])
            else:
                x, size = query[1], query[2]

                if size > x:
                    ans.append(False)
                    continue

                max_value = seg.query(0,x-size)
                ans.append(max_value >= size)

        return ans
                
