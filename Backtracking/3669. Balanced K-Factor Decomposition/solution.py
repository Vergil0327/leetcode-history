class Solution:
    def minDifference(self, n: int, k: int) -> List[int]:
        factors = set()
        for i in range(1, int(sqrt(n))+1):
            if n%i == 0:
                factors.add(i)
                factors.add(n//i)
        
        self.res = []
        self.diff = float('inf')
        def dfs(n, k, cur):
            if k == 1:
                arr = cur + [n]
                mx, mn = max(arr), min(arr)
                if (x := mx-mn) < self.diff:
                    self.diff = x
                    self.res = arr
                return

            for f in factors:
                if n%f == 0:
                    dfs(n//f, k-1, cur + [f])
        dfs(n, k, [])
        return self.res