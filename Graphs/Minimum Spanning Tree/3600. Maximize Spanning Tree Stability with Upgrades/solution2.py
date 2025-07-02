# binary search solution

class UnionFind:
    def __init__(self, n: int) -> None:
        self.rank = [1] * n
        self.parent = [i for i in range(n)]

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return False
        
        if self.rank[px] < self.rank[py]:
            px, py = py, px

        self.parent[py] = px
        self.rank[px] += self.rank[py]
        return True

    def is_connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)
    

class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        initial_uf = UnionFind(n)
        # Observation 1: Find minimum s_i for must-have edges.
        min_s = inf
        for u, v, s, must in edges:
            if not must: continue
            min_s = min(min_s, s)

            # Observation 2: The must-have edges form a cycle.
            if not initial_uf.union(u, v):
                return -1
        
        def check(min_stability: int) -> bool:
            # Observation 1
            if min_stability > min_s:
                return False
            
            # This copies the initial state, where all `must-have edges`
            # are connected.
            uf = UnionFind(n)
            uf.rank, uf.parent = initial_uf.rank[:], initial_uf.parent[:]

            # Observation 3: List of edges to consider an upgrade
            upgrade = []
            for u, v, s, must in edges:
                if must: continue
                # Observation 3
                if s >= min_stability:
                    uf.union(u, v)
                elif s * 2 >= min_stability:
                    upgrade.append((u, v))

            remaining = k  # number of upgrades remaining
            # The following edge selection method will not waste our chances to
            # upgrade. See proof below.
            for u, v in upgrade:
                if uf.is_connected(u, v): continue
                if remaining == 0: return False
                uf.union(u, v)
                remaining -= 1
            
            # Observation 3
            return all(uf.find(i) == uf.find(0) for i in range(n))

        l, r = -1, max(s for _, _, s, _ in edges) * 2
        while l < r:
            mid = r - (r-l) // 2
            if check(mid):
                l = mid
            else:
                r = mid - 1
        return l