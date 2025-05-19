class Solution:
    def minimumWeight(self, edges, queries):
        n = len(edges) + 1
        LOG = n.bit_length()
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append([v, w])
            graph[v].append([u, w])

        # binary lifting
        up = [[-1] * n for _ in range(LOG)]
        depth = [0] * n
        dist0 = [0] * n

        queue = [0]
        for u in queue:
            for v, w in graph[u]:
                if v != up[0][u]:
                    up[0][v] = u
                    depth[v] = depth[u] + 1
                    dist0[v] = dist0[u] + w
                    queue.append(v)
        
        for k in range(LOG - 1):
            for v in range(n):
                p = up[k][v]
                up[k+1][v] = -1 if p < 0 else up[k][p]

        def lca(a, b):
            if depth[a] < depth[b]:
                a, b = b, a
            diff = depth[a] - depth[b]
            for k in range(LOG):
                if (diff >> k) & 1:
                    a = up[k][a]
            if a == b:
                return a
            for k in reversed(range(LOG)):
                if up[k][a] != up[k][b]:
                    a = up[k][a]
                    b = up[k][b]
            return up[0][a]

        def dist(a, b):
            c = lca(a, b)
            return dist0[a] + dist0[b] - 2 * dist0[c]

        ans = []
        for src1, src2, target in queries:
            d12 = dist(src1, src2)
            d1t = dist(src1, target)
            d2t = dist(src2, target)
            ans.append((d12 + d1t + d2t) // 2)
        return ans