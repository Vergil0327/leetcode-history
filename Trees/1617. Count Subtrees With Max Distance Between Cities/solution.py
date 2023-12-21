class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in edges:
            u, v = u-1, v-1
            graph[u].append(v)
            graph[v].append(u)

        dist = [[inf]*n for _ in range(n)]

        for node in range(n):
            dist[node][node] = 0
        for src in range(n):
            for dst in graph[src]:
                dist[src][dst] = 1

        for mid in range(n):
            for src in range(n):
                for dst in range(n):
                    if src == dst: continue
                    dist[src][dst] = min(dist[src][dst], dist[src][mid] + dist[mid][dst])

        def checkValidSubtree(state):
            start = -1
            for i in range(n):
                if (state>>i)&1:
                    start = i
                    break

            queue = deque([start])
            connected = visited = 0
            while queue:
                node = queue.popleft()
                if (visited>>node)&1: continue
                visited |= 1<<node
                connected += 1

                for nei in graph[node]:
                    if (state>>nei)&1 == 0: continue
                    if (visited>>nei)&1: continue
                    queue.append(nei)
            return connected == state.bit_count()
            
            # parent = list(range(n))
            # def find(x):
            #     if parent[x] != x:
            #         parent[x] = find(parent[x])
            #     return parent[x]
            # def union(x, y):
            #     px, py = find(x), find(y)
            #     if px == py: return
            #     if px <= py:
            #         parent[py] = px
            #     else:
            #         parent[px] = py

            # nodes = set()
            # for i in range(n):
            #     if (state>>i)&1:
            #         nodes.add(i)

            # for node in nodes:
            #     for nei in graph[node]:
            #         if nei in nodes:
            #             union(node, nei)
            
            # return len(set(find(node) for node in nodes)) == 1

        maxState = 1<<n

        res = [0]*(n-1)
        state = maxState-1
        submask = state
        while submask > 0:
            if submask.bit_count()>1 and checkValidSubtree(submask):
                nodes = []
                for i in range(n):
                    if (submask>>i)&1:
                        nodes.append(i)

                m = len(nodes)
                mxDist = 0
                for i in range(m):
                    for j in range(i+1, m):
                        mxDist = max(mxDist, dist[nodes[i]][nodes[j]])
                res[mxDist-1] += 1
            submask = (submask-1)&state
        return res
