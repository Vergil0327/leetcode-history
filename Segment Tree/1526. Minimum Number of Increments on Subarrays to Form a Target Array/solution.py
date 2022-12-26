# Segment Tree + Recursion
class Seg():
    def __init__(self, nums, op=min):
        n = len(nums)
        self.op = op
        self.n = n
        self.tree = [[0, 0] for _ in range(2*n)]


        for i in range(n, 2*n):
            self.tree[i][0] = nums[i-n]
            self.tree[i][1] = i-n

        # 1-based
        for i in range(n-1, 0, -1):
            self.tree[i][0] = op(self.tree[i<<1][0], self.tree[i<<1|1][0])
            self.tree[i][1] = self.tree[i<<1][1] if self.tree[i<<1][0] == self.tree[i][0] else self.tree[i<<1|1][1]

    def query(self, l, r):
        tree, op, n = self.tree, self.op, self.n
        l, r = l+n, r+n

        res = inf
        pos = -1
        while l <= r:
            if l == r:
                res = op(res, tree[l][0])
                if tree[l][0] == res:
                    pos = tree[l][1]
                break

            if l&1 == 1:
                res = op(res, tree[l][0])
                if tree[l][0] == res:
                    pos = tree[l][1]
                l += 1

            if r&1 == 0:
                res = op(res, tree[r][0])
                if tree[r][0] == res:
                    pos = tree[r][1]
                r -= 1
            l, r = l>>1, r>>1
        return res, pos

class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        n = len(target)
        seg = Seg(target)

        def dfs(l, r, base):
            if l > r: return 0
            if l == r: return target[l]-base

            rangeMin, idx = seg.query(l, r)

            inc = rangeMin-base
            inc += dfs(l, idx-1, rangeMin)
            inc += dfs(idx+1, r, rangeMin)
            return inc
            
        return dfs(0, n-1, 0)


# Greedy
class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        n = len(target)
        res, currHeight = 0, 0
        for i in range(n):
            if target[i] > currHeight:
                res += target[i]-currHeight
            currHeight = target[i]
        return res