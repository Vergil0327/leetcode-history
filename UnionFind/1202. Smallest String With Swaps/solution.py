class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)

        # union-find
        parent = list(range(n))
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            if x < y:
                parent[y] = x
            else:
                parent[x] = y

        # find connected components
        for i, j in pairs:
            pi, pj = find(i), find(j)
            if pi == pj: continue
            union(pi, pj)

        groups = defaultdict(list)
        indices = defaultdict(list)
        for idx in range(n):
            groups[find(idx)].append(s[idx])
            indices[find(idx)].append(idx)

        # sort each connected component and replace
        res = list(s)
        for key, chList in groups.items():
            chList.sort()
            i = 0
            for idx in indices[key]:
                res[idx] = chList[i]
                i += 1
        return "".join(res)