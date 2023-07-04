class Solution:
    def findLatestStep(self, arr: List[int], target: int) -> int:
        n = len(arr)
        bits = [0]*(n+2)

        parent = list(range(n+2))
        size = [0]*(n+2)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        exists = defaultdict(int)
        def union(x, y):
            px, py = find(x), find(y)
            if px == py: return
            if size[py] == 0:
                return # only union if there exists bit 1

            m, n = size[px], size[py]
            if m <= n:
                parent[px] = py
                size[py] += size[px]
            else:
                parent[py] = px
                size[px] += size[py]

            exists[m] -= 1
            if exists[m] == 0:
                del exists[m]
            exists[n] -= 1
            if exists[n] == 0:
                del exists[n]
            exists[m+n] += 1

        latestStep = -1
        for step, i in enumerate(arr, start=1):
            if bits[i]: continue
            bits[i] = 1
            size[i] = 1
            exists[size[i]] += 1

            union(i, i-1)
            union(i, i+1)

            if target in exists:
                latestStep = step

        return latestStep