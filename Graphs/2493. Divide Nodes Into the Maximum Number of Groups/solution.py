
# Accepted - optimzed from brute force
# we can check validity of connected component in BFS
class Solution_Optimized:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n+1)]
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px <= py:
                parent[py] = px
            else:
                parent[px] = py

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            union(u, v)

        # we need to find every connected components
        connected = defaultdict(list)
        for i in range(1, n+1):
            connected[find(parent[i])].append(i)

        # calculate max groups in each connected component
        # also check if there exists odd length cycle
        # how to check validity ?
        def BFS(start):
            queue = deque([[start, 1]]) # node, layer
            groups = 0
            visited = {start: 1}
            while queue:
                sz = len(queue)
                for _ in range(sz):
                    node, layer = queue.popleft()

                    for nxt in graph[node]:
                        if nxt not in visited:
                            nextLayer = layer+1
                            visited[nxt] = nextLayer
                            queue.append([nxt, nextLayer])
                        else:
                            if visited[nxt] == layer: return -1
                groups += 1
            return groups

        maxGroups = 0
        for nodes in connected.values():
            count = 0
            # if we want to find maximum group of current connected component,
            # we need to use every node as starting point to traverse in BFS way to find max groups
            for node in nodes:
                cnt = BFS(node)
                if cnt == -1: return -1
                count = max(count, cnt)

            maxGroups += count
        return maxGroups

# beats 100% of python3 programs
class Solution_MOST_OPTIMIZED:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n+1)]
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px <= py:
                parent[py] = px
            else:
                parent[px] = py

        indegree = [0] * (n+1)
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            union(u, v)
            indegree[u] += 1
            indegree[v] += 1
            
        # calculate max groups
        # also check if there exists odd length cycle
        def BFS(start):
            queue = deque([[start, 1]]) # node, layer
            groups = 0
            visited = {start: 1}
            while queue:
                sz = len(queue)
                for _ in range(sz):
                    node, layer = queue.popleft()

                    for nxt in graph[node]:
                        if nxt not in visited:
                            nextLayer = layer+1
                            visited[nxt] = nextLayer
                            queue.append([nxt, nextLayer])
                        else:
                            if visited[nxt] == layer: return -1
                groups += 1
            return groups
        
        # find connected components
        groups = defaultdict(list)
        for i in range(1, n+1):
            groups[find(parent[i])].append(i)

        def findOuterMost(nodes):
            outer = []
            degrees = []
            for node in nodes:
                degrees.append(indegree[node])
            minDeg = min(degrees)
            for node in nodes:
                if indegree[node] == minDeg:
                    outer.append(node)
            return outer

        maxGroups = 0
        for nodes in groups.values():
            count = 0
            
            # find all the outer-most node
            # max levels of BFS only comes from outer-most node as starting point
            outer = findOuterMost(nodes)
            
            for node in outer:
                cnt = BFS(node)
                if cnt == -1: return -1
                count = max(count, cnt)

            maxGroups += count
        return maxGroups

# Brute Force
# 1. use union-find to get all the connected components
# 2. find each connected component's max groups
# 3. sum up all the max groups of each connected component
# 4. if one of connected component is invalid, return -1
class Solution_TLE:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n+1)]
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px <= py:
                parent[py] = px
            else:
                parent[px] = py

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            union(u, v)
            
        # calculate max groups in each connected component
        # also check if there exists odd length cycle
        
        # how to check validity ?
        def isBipartite(node):
            color = [False] * 505 # n <= 500
            visited = set([node])
            def dfs(node):
                for nei in graph[node]:
                    if nei in visited:
                        if color[nei] == color[node]:
                            return False
                        continue

                    visited.add(nei)
                    color[nei] = not color[node]
                    if not dfs(nei): return False
                        
                return True
            return dfs(node)

        def BFS(start):
            queue = deque([start])
            groups = 0
            visited = set()
            while queue:
                sz = len(queue)
                for _ in range(sz):
                    node = queue.popleft()

                    visited.add(node)
                    for nxt in graph[node]:
                        if nxt not in visited:
                            queue.append(nxt)
                groups += 1
            return groups
        
        # we need to find maximum group within each group's nodes
        # traverse all the nodes to find max
        groups = defaultdict(list)
        for i in range(1, n+1):
            groups[find(parent[i])].append(i)

        maxGroups = 0
        for root, nodes in groups.items():
            if not isBipartite(root): return -1
            count = 0
            for node in nodes:
                count = max(count, BFS(node))

            maxGroups += count
        return maxGroups
