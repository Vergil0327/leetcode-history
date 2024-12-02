class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        graph1, graph2 = defaultdict(list), defaultdict(list)
        for u, v in edges1:
            graph1[u].append(v)
            graph1[v].append(u)

        for u, v in edges2:
            graph2[u].append(v)
            graph2[v].append(u)

        n, m = len(edges1) + 1, len(edges2) + 1

        @cache
        def dfs1(node, prev, isEven):
            res = isEven
            for nxt in graph1[node]:
                if nxt == prev:
                    continue
                res += dfs1(nxt, node, 1 - isEven)
            return res

        def reroot1(node, prev, count):
            for nxt in graph1[node]:
                if nxt == prev:
                    continue
                countEven[nxt] = n - count
                reroot1(nxt, node, n - count)

        countEven = Counter()
        countEven[0] = dfs1(0, -1, 1)
        reroot1(0, -1, countEven[0])

        @cache
        def dfs2(node, prev, isEven):
            res = isEven
            for nxt in graph2[node]:
                if nxt == prev:
                    continue
                res += dfs2(nxt, node, 1 - isEven)
            return res

        def reroot2(node, prev, count):
            for nxt in graph2[node]:
                if nxt == prev:
                    continue
                countOdd[nxt] = m - count
                reroot2(nxt, node, m - count)

        countOdd = Counter()
        countOdd[0] = dfs2(0, -1, 0)
        reroot2(0, -1, countOdd[0])

        best = max(countOdd.values())
        return [countEven[node] + best for node in range(n)]
