class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        # find & group together all the connected nodes
        parent = list(range(c+1))
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            px, py = find(x), find(y)
            if px==py: return

            if px > py:
                px, py = py, px
            parent[py] = px

        for u, v in connections:
            union(u, v)

        # use root node as key and put all the connected nodes in SortedSet[key]
        s = defaultdict(SortedSet)
        for i in range(1, c+1):
            parent[i] = find(i)
            s[parent[i]].add(i)

        # we can easily check & find smallest valid node through SortedSet[parent[node]]
        res = []
        for typ, x in queries:
            key = parent[x]
            if typ == 1:
                if x in s[key]:
                    res.append(x)
                else:
                    res.append(-1 if not s[key] else s[key][0])
            else:
                s[key].discard(x)
        return res
