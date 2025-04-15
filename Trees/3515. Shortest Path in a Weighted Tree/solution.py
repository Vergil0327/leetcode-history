
class Fenwick:
    def __init__(self, n):
        self.a = [0] * (n + 1)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.a[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i < len(self.a):
            self.a[i] += x
            i += i & -i
            
class Solution:
    def treeQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        weight = {}
        for u,v,w in edges:
            u -= 1
            v -= 1
            graph[u].append([v,w])
            graph[v].append([u,w])

            if v<u: u,v=v,u
            weight[u, v] = w

        t_in = [0] * n
        t_out = [0] *n
        dist = [0] * n
        parent = [0] *n
        timer = 0

        def dfs(u, p):
            nonlocal timer
            parent[u] = p
            timer += 1
            t_in[u] = timer

            for v, w in graph[u]:
                if v != p:
                    dist[v] = dist[u] + w
                    dfs(v, u)

            t_out[u] = timer
            timer += 1

        dfs(0, -1)

        fen = Fenwick(timer)
        ans = []
        for cmd, *query in queries:
            if cmd == 1:
                u,v,w = query
                u -= 1
                v -= 1
                if parent[u] == v:
                    node = u
                elif parent[v] == u:
                    node = v
                else:
                    continue

                key = min(u,v), max(u,v)
                w1 = weight[key]
                weight[key] = w
                fen.add(t_in[node], w - w1)
                fen.add(t_out[node]+1, w1 - w)
            elif cmd == 2:
                node, = query
                node -= 1
                delta = fen.sum(t_in[node])
                ans.append(dist[node] + delta)

        return ans
