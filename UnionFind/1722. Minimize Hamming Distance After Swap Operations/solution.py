class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        
        parent = list(range(n))
        rank = [1] * n
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        for x, y in allowedSwaps:
            px, py = find(x), find(y)
            if px == py: continue
            
            if rank[px] >= rank[py]:
                parent[py] = px
                rank[px] += rank[py]
            else:
                parent[px] = py
                rank[py] += rank[px]

        counter = [Counter() for i in range(n)]
        for i in range(n):
            counter[find(i)][source[i]] += 1

        res = 0
        for i in range(n):
            p = find(i)
            group = counter[p]

            if target[i] in group:
                group[target[i]] -= 1
                if group[target[i]] == 0:
                    del group[target[i]]
            else:
                res += 1
        return res