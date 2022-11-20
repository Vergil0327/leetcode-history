# Topological Sort
class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        if not roads: return 0
        n = len(roads)
        
        inDegrees = [0] * (n+1)
        G = defaultdict(list)
        for u, v in roads:
            G[u].append(v)
            inDegrees[v] += 1
            G[v].append(u)
            inDegrees[u] += 1
            
        queue = deque()
        for i, deg in enumerate(inDegrees):
            # ! if we got a linked-list we don't want to count capital
            # ex [[0,1],[1,2]], 3
            if deg == 1 and i != 0: # don't include capital(i=0)
                queue.append(i) # city
        capicity = [1] * (n+1)

        cnt = 0
        while queue:

            sz = len(queue)
            for _ in range(sz):
                node = queue.popleft()
                cnt += math.ceil(capicity[node]/seats)
                # cnt += (capicity[node]+seats-1)//seats
                
                for nxt in G[node]:
                    capicity[nxt] += capicity[node]
                    inDegrees[nxt] -= 1
                    if inDegrees[nxt] == 1 and nxt != 0: # don't include capital
                        queue.append(nxt)

        return cnt

# DFS
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
            
            # print(curr, person, seats)
            if curr != 0:
                self.liter += math.ceil(person/seats) # slow
                # self.liter += (person+seats-1)//seats # integer is more efficient
            return person
        dfs(0, -1)
        return self.liter
