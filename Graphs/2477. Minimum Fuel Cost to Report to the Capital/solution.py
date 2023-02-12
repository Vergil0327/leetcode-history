# Topological Sort
class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        n = len(roads)

        graph = defaultdict(list)
        indegree = [0] * (n+1)
        for u, v in roads:
            graph[u].append(v)
            graph[v].append(u)
            indegree[v] += 1
            indegree[u] += 1

        queue = deque()
        CAPITAL = 0
        for node, deg in enumerate(indegree):
            # ! if we got a linked-list we don't want to count capital
            # ex [[0,1],[1,2]], 3
            if deg == 1 and node != CAPITAL: # don't include capital(node=0)
                queue.append(node) # city

        capacity = [1] * (n+1)
        fuel = 0
        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                fuel += int(ceil(capacity[curr]/seats))
                # fuel += (capicity[node]+seats-1)//seats

                for nxt in graph[curr]:
                    capacity[nxt] += capacity[curr]
                    indegree[nxt] -= 1
                    if indegree[nxt] == 1 and nxt != CAPITAL: # don't include capital
                        queue.append(nxt)
        return fuel

# DFS
"""
break down into many subproblem
we can calculate fuel in post-order DFS position
"""
class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        if not roads: return 0

        G = defaultdict(list)
        for u, v in roads:
            G[u].append(v)
            G[v].append(u)

        self.liter = 0
        def dfs(curr, parent):
            person = 1
            for nxt in G[curr]:
                if nxt != parent:
                    person += dfs(nxt, curr)
            
            if curr != 0:
                self.liter += math.ceil(person/seats) # slow
                # self.liter += (person+seats-1)//seats # integer is more efficient
            return person
        dfs(0, -1)
        return self.liter
    
class ConciseSolution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        graph = defaultdict(list)
        for u, v in roads:
            graph[u].append(v)
            graph[v].append(u)

        fuel = 0
        def dfs(node, parent):
            nonlocal fuel
            people = 0
            for nxt in graph[node]:
                if nxt == parent: continue
                passengers = dfs(nxt, node)
                people += passengers
                fuel += int(ceil(passengers/seats))

            return people + 1 # current node itself 

        dfs(0, -1)
        return fuel
