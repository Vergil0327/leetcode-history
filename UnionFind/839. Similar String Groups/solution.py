class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n, m = len(strs), len(strs[0])
        parent = list(range(n))
        rank = [1]*n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            if rank[px] <= rank[py]:
                parent[px] = py
                rank[py] += rank[px]
            else:
                parent[py] = px
                rank[px] += rank[py]

        def oneSwapClose(x, y):
            diff = 0
            for i in range(m):
                if x[i] != y[i]:
                    diff += 1
                if diff > 2: return False
            return diff <= 2

        isSimilar = [[False]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j: continue
                if oneSwapClose(strs[i], strs[j]):
                    isSimilar[i][j] = True

        for i in range(n):
            for j in range(n):
                if i == j: continue

                px, py = find(i), find(j)
                if px == py: continue
                if isSimilar[i][j]:
                    union(i, j)

        return len(set(parent))