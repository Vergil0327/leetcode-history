class SegmentTree:
    def __init__(self, n, op=sum):
        self.n = n
        self.st = st = [0]*(2*n)
        self.op = op

    def __getitem__(self, i):
        return self.st[i+self.n]
    def __setitem__(self, i, v):
        st, op, n = self.st, self.op, self.n
        i += n
        st[i] = v

        while i:
            st[i>>1] = op([st[i], st[i^1]])
            i >>= 1

    def countLessThan(self, pos):
      st, op, n = self.st, self.op, self.n
      l,r = n, pos+n

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
    
    # query [l,r] both inclusive
    def query(self, l, r):
      st, op, n = self.st, self.op, self.n
      l,r = l+n, r+n

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

class Solution:
    def minInteger(self, num: str, k: int) -> str:
        n = len(num)
        position = defaultdict(deque)
        for i in range(n):
            position[num[i]].append(i)

        seg = SegmentTree(n)        
        res = ""
        for i in range(n):
            for d in range(10):
                d = str(d)
                if len(position[d]) > 0:
                    pos = position[d][0]
                    shift = seg.countLessThan(pos)
                    
                    if (swap := pos - shift) <= k:
                        res += d

                        k -= swap
                        seg[pos] = seg[pos] + 1
                        position[d].popleft()
                        break
        return res