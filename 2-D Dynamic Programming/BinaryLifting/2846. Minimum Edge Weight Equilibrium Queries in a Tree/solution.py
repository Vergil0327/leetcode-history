class Solution:
    def minOperationsQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append([w, v])
            graph[v].append([w, u])

        m = n.bit_length()
        # parent[i][j] means 2^i -th parent of node j
        parent = [[0]*n for _ in range(m)]

        # occurence[i][j] means the number of edges of j weight from root to node i
        occurence = [[0]*27 for _ in range(n)]
        
        # depth[i]: the depth of node i
        count = [0]*n

        def dfs(node, prev, depth):
            parent[0][node] = prev
            count[node] = depth
            for w, nei in graph[node]:
                if prev == nei: continue
                occurence[nei] = occurence[node].copy()
                occurence[nei][w] += 1
                dfs(nei, node, depth+1)
        dfs(0, 0, 0)
        
        # build binary lifting table
        for i in range(1, m):
            for j in range(n):
                # x = j take 2^(i-1) depth
                # j take 2^i-th depth = x take 2^(i-1) depth
                x = parent[i-1][j]
                parent[i][j] = parent[i-1][x]

        @cache
        def lca(u, v):
            # make count[v]-count[u] positive
            if count[u] > count[v]:
                return lca(v, u)

            # move v to same depth as u
            for i in range(m):
                if ((count[v]-count[u])>>i)&1:
                    v = parent[i][v]

            if u == v: return u

            for i in range(m-1, -1, -1):
                if parent[i][u] != parent[i][v]:
                    u = parent[i][u]
                    v = parent[i][v]
            return u if u == v else parent[0][u]

        res = []
        for u, v in queries:
            k = lca(u, v)

            numEdges = count[u] + count[v] - 2 * count[k]
            numMaxEdges = max(occurence[u][w] + occurence[v][w] - 2 * occurence[k][w] for w in range(1, 27))
            res.append(numEdges - numMaxEdges)
        return res
