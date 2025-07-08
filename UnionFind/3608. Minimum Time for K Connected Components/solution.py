class Solution:
    def minTime(self, n: int, edges: List[List[int]], k: int) -> int:
        def count(t):
            parent = list(range(n))
            rank = [1] * n

            def find(x):
                if parent[x] != x:
                    parent[x] = find(parent[x])
                return parent[x]
            def union(x, y):
                px, py = find(x), find(y)
                if px == py: return

                if rank[px] < rank[py]:
                    px, py = py, px
                parent[py] = px
                rank[px] += rank[py]

            for u, v, time in edges:
                if time > t:
                    union(u, v)

            return len(set(find(x) for x in range(n)))

        l, r = 0, 10**9
        while l < r:
            t = l + (r-l)//2

            if count(t) >= k:
                r = t
            else:
                l = t+1
        return l
        

class Solution:
    def minTime(self, n: int, edges: List[List[int]], k: int) -> int:
        if not edges:
            return 0
        edges.sort(key = lambda e: -e[2])

        f = [i for i in range(n)]

        def find(x):
            if x == f[x]:
                return x
            f[x] = find(f[x])
            return f[x]

        def union(x, y):
            x = find(x)
            y = find(y)
            if x == y:
                return False
            f[x] = y
            return True

        count = n
        for u, v, t in edges:
            if union(u, v):
                count -= 1
            if count < k:
                return t
        return 0